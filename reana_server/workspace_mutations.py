# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Cross-process serialization for shared-workspace mutations."""

import hashlib
import logging
import os
import threading
from contextlib import contextmanager

from reana_db.config import SQLALCHEMY_DATABASE_URI
from reana_db.database import Session
from sqlalchemy import create_engine, text
from sqlalchemy.pool import NullPool


class WorkspaceMutationConflict(Exception):
    """Another operation currently owns one of the requested workspaces."""


class WorkspaceMutationUnavailable(Exception):
    """Workspace serialization infrastructure is unavailable."""


_engine = None
_engine_guard = threading.Lock()
_local_locks = {}
_local_locks_guard = threading.Lock()


def _get_lock_engine():
    """Return the lazy, unpooled engine reserved for advisory locks.

    ``NullPool`` keeps advisory-lock checkouts independent from the ORM pool.
    Synchronous validation can prolong a lock checkout; moving that wait off the
    request path is tracked in reanahub/reana-workflow-validator#9.
    """
    global _engine
    if _engine is None:
        with _engine_guard:
            if _engine is None:
                _engine = create_engine(
                    SQLALCHEMY_DATABASE_URI,
                    poolclass=NullPool,
                    pool_pre_ping=True,
                )
    return _engine


def _normalise_paths(workspace_paths):
    """Return unique absolute workspace paths in deadlock-safe order."""
    return sorted({os.path.abspath(os.fspath(path)) for path in workspace_paths})


def _workflow_family_key(owner_id, workflow_name):
    """Return an opaque lock key shared by all runs of one workflow name."""
    identity = "{}\0{}".format(owner_id, workflow_name).encode("utf-8")
    return "workflow-family:" + hashlib.sha256(identity).hexdigest()


@contextmanager
def _mutation_locks(keys):
    """Own a normalized set of opaque mutation keys."""
    keys = sorted(set(keys))
    if not keys:
        yield
        return
    if Session.get_bind().dialect.name == "postgresql":
        with _postgresql_locks(keys):
            yield
    else:
        with _local_process_locks(keys):
            yield


def _advisory_key(workspace_path):
    """Map a normalized workspace path to a signed PostgreSQL bigint."""
    return int.from_bytes(
        hashlib.sha256(workspace_path.encode("utf-8")).digest()[:8],
        byteorder="big",
        signed=True,
    )


def _release_postgresql_locks(connection, transaction):
    """Best-effort release that never masks the protected operation's result."""
    if transaction is not None and transaction.is_active:
        try:
            transaction.rollback()
        except Exception as error:
            logging.exception("Could not roll back workspace-lock transaction.")
            try:
                connection.invalidate(error)
            except Exception:
                logging.exception("Could not invalidate workspace-lock connection.")
    if connection is not None:
        try:
            connection.close()
        except Exception:
            logging.exception("Could not close workspace-lock connection.")


@contextmanager
def _postgresql_locks(workspace_paths):
    """Own transaction-scoped advisory locks on a dedicated connection."""
    connection = None
    transaction = None
    try:
        connection = _get_lock_engine().connect()
        transaction = connection.begin()
        for workspace_path in workspace_paths:
            acquired = connection.execute(
                text("SELECT pg_try_advisory_xact_lock(:key)"),
                {"key": _advisory_key(workspace_path)},
            ).scalar()
            if not acquired:
                raise WorkspaceMutationConflict()
    except WorkspaceMutationConflict:
        _release_postgresql_locks(connection, transaction)
        raise
    except Exception as error:
        _release_postgresql_locks(connection, transaction)
        raise WorkspaceMutationUnavailable() from error

    try:
        yield
    finally:
        # The lock-only transaction has nothing to commit. Rollback releases
        # every xact lock and cleanup errors must not turn a completed mutation
        # into a retryable response-after-success ambiguity.
        _release_postgresql_locks(connection, transaction)


@contextmanager
def _local_process_locks(workspace_paths):
    """Own refcounted process-local locks for non-PostgreSQL development."""
    entries = []
    acquired = []
    with _local_locks_guard:
        for workspace_path in workspace_paths:
            entry = _local_locks.get(workspace_path)
            if entry is None:
                entry = {"lock": threading.Lock(), "references": 0}
                _local_locks[workspace_path] = entry
            entry["references"] += 1
            entries.append((workspace_path, entry))
    try:
        for _workspace_path, entry in entries:
            if not entry["lock"].acquire(blocking=False):
                raise WorkspaceMutationConflict()
            acquired.append(entry["lock"])
        yield
    finally:
        for lock in reversed(acquired):
            lock.release()
        with _local_locks_guard:
            for workspace_path, entry in entries:
                entry["references"] -= 1
                if entry["references"] == 0:
                    _local_locks.pop(workspace_path, None)


@contextmanager
def workspace_mutation_locks(workspace_paths):
    """Serialize mutations of one or more workspaces without waiting."""
    normalized_paths = _normalise_paths(workspace_paths)
    with _mutation_locks(normalized_paths):
        yield


@contextmanager
def workspace_mutation_lock(workspace_path):
    """Serialize mutation of a single shared workspace."""
    with workspace_mutation_locks([workspace_path]):
        yield


@contextmanager
def workflow_family_mutation_lock(owner_id, workflow_name):
    """Serialize operations that can add or remove runs of one workflow name."""
    with _mutation_locks([_workflow_family_key(owner_id, workflow_name)]):
        yield


@contextmanager
def workflow_creation_mutation_lock(owner_id, workflow_name, workspace_path):
    """Reserve a workflow family and its preallocated workspace together."""
    with _mutation_locks(
        [
            _workflow_family_key(owner_id, workflow_name),
            os.path.abspath(os.fspath(workspace_path)),
        ]
    ):
        yield
