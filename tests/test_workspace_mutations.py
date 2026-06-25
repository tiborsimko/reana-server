# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Tests for shared-workspace mutation serialization."""

from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest

from reana_server import workspace_mutations
from reana_server.workspace_mutations import (
    WorkspaceMutationConflict,
    WorkspaceMutationUnavailable,
    workflow_creation_mutation_lock,
    workflow_family_mutation_lock,
    workspace_mutation_lock,
    workspace_mutation_locks,
)


def _postgresql_connection(results):
    """Build a lock engine connection yielding the requested scalar results."""
    transaction = Mock(is_active=True)
    connection = Mock()
    connection.begin.return_value = transaction
    connection.execute.side_effect = [
        Mock(scalar=Mock(return_value=value)) for value in results
    ]
    engine = Mock()
    engine.connect.return_value = connection
    return engine, connection, transaction


def test_local_lock_conflict_and_registry_eviction(tmp_path):
    """Local fallback rejects overlap and does not retain workspace keys."""
    workspace = str(tmp_path / "workspace")
    with patch.object(
        workspace_mutations.Session,
        "get_bind",
        return_value=SimpleNamespace(dialect=SimpleNamespace(name="sqlite")),
    ):
        with workspace_mutation_lock(workspace):
            with pytest.raises(WorkspaceMutationConflict):
                with workspace_mutation_lock(workspace):
                    pass
        assert workspace_mutations._local_locks == {}


def test_creation_reserves_family_and_workspace(tmp_path):
    """Creation collides with both family deletion and workspace mutation."""
    workspace = str(tmp_path / "workspace")
    with patch.object(
        workspace_mutations.Session,
        "get_bind",
        return_value=SimpleNamespace(dialect=SimpleNamespace(name="sqlite")),
    ):
        with workflow_creation_mutation_lock("owner", "analysis", workspace):
            with pytest.raises(WorkspaceMutationConflict):
                with workflow_family_mutation_lock("owner", "analysis"):
                    pass
            with pytest.raises(WorkspaceMutationConflict):
                with workspace_mutation_lock(workspace):
                    pass
        assert workspace_mutations._local_locks == {}


def test_postgresql_locks_are_deduplicated_and_sorted(tmp_path):
    """Multi-workspace acquisition uses one transaction and stable ordering."""
    first = str(tmp_path / "a")
    second = str(tmp_path / "b")
    engine, connection, transaction = _postgresql_connection([True, True])
    with patch.object(
        workspace_mutations.Session,
        "get_bind",
        return_value=SimpleNamespace(dialect=SimpleNamespace(name="postgresql")),
    ), patch.object(workspace_mutations, "_get_lock_engine", return_value=engine):
        with workspace_mutation_locks([second, first, second]):
            pass

    assert [call.args[1]["key"] for call in connection.execute.call_args_list] == [
        workspace_mutations._advisory_key(first),
        workspace_mutations._advisory_key(second),
    ]
    transaction.rollback.assert_called_once_with()
    connection.close.assert_called_once_with()


def test_postgresql_contention_releases_acquired_locks():
    """A failed later key rolls back all earlier transaction locks."""
    engine, connection, transaction = _postgresql_connection([True, False])
    with patch.object(workspace_mutations, "_get_lock_engine", return_value=engine):
        with pytest.raises(WorkspaceMutationConflict):
            with workspace_mutations._postgresql_locks(["a", "b"]):
                pass
    transaction.rollback.assert_called_once_with()
    connection.close.assert_called_once_with()


def test_postgresql_acquisition_failure_is_unavailable():
    """Database failures before the callback map to infrastructure failure."""
    engine, connection, transaction = _postgresql_connection([])
    connection.execute.side_effect = RuntimeError("database unavailable")
    with patch.object(workspace_mutations, "_get_lock_engine", return_value=engine):
        with pytest.raises(WorkspaceMutationUnavailable):
            with workspace_mutations._postgresql_locks(["a"]):
                pass
    transaction.rollback.assert_called_once_with()
    connection.close.assert_called_once_with()


def test_postgresql_cleanup_failure_does_not_override_success():
    """Cleanup trouble cannot create a retry-after-success ambiguity."""
    engine, connection, transaction = _postgresql_connection([True])
    transaction.rollback.side_effect = RuntimeError("connection dropped")
    with patch.object(workspace_mutations, "_get_lock_engine", return_value=engine):
        with workspace_mutations._postgresql_locks(["a"]):
            completed = True
    assert completed
    connection.invalidate.assert_called_once()
    connection.close.assert_called_once_with()


def test_lock_engine_is_isolated_and_unpooled():
    """Advisory locks use a dedicated NullPool engine, never the ORM pool.

    This is the isolation invariant behind PR794-26: a lock checkout cannot
    draw from (and therefore cannot exhaust) reana-db's shared ORM connection
    pool. A full multi-thread, production-pool-limit regression test additionally
    requires a live PostgreSQL backend and belongs in the DB-backed suite.
    """
    from sqlalchemy.pool import NullPool

    with patch.object(
        workspace_mutations, "SQLALCHEMY_DATABASE_URI", "postgresql://u:p@localhost/db"
    ), patch.object(workspace_mutations, "_engine", None):
        engine = workspace_mutations._get_lock_engine()
        assert isinstance(engine.pool, NullPool)
        # The engine is lazily built once and reused across acquisitions.
        assert workspace_mutations._get_lock_engine() is engine
