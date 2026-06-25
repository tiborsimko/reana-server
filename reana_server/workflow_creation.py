# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Reconcile ambiguous workflow-controller creation failures."""

import logging
import os
import time

from bravado.exception import HTTPError

from reana_db.database import Session
from reana_db.models import Workflow

_CREATION_RECONCILIATION_TIMEOUT = 1.0
_CREATION_RECONCILIATION_INTERVAL = 0.1


def _find_created_workflow(workflow_uuid, user_id):
    """Return the freshly committed workflow, bypassing stale ORM state."""
    Session.rollback()
    return (
        Session.query(Workflow)
        .filter(Workflow.id_ == workflow_uuid, Workflow.owner_id == user_id)
        .first()
    )


def _reconcile_failed_creation(
    workflow_uuid,
    user_id,
    workspace_path,
    compensate,
    wait_for_commit,
):
    """Compensate a controller-created row while its server lock is held."""
    deadline = time.monotonic() + (
        _CREATION_RECONCILIATION_TIMEOUT if wait_for_commit else 0
    )
    while True:
        workflow = _find_created_workflow(workflow_uuid, user_id)
        if workflow is not None:
            if os.path.abspath(workflow.workspace_path) != os.path.abspath(
                workspace_path
            ):
                logging.error(
                    "Controller created workflow %s with an unexpected workspace.",
                    workflow_uuid,
                )
                return False
            compensate(workflow)
            return True
        if time.monotonic() >= deadline:
            return False
        time.sleep(_CREATION_RECONCILIATION_INTERVAL)


def create_workflow_on_controller(
    create,
    workflow_uuid,
    user_id,
    workspace_path,
    compensate,
):
    """Call RWC and compensate visible commits after ambiguous failures.

    The caller must own the workflow-creation mutation lock for this complete
    call, including reconciliation.
    """
    try:
        return create()
    except HTTPError as error:
        if error.response.status_code >= 500:
            try:
                _reconcile_failed_creation(
                    workflow_uuid,
                    user_id,
                    workspace_path,
                    compensate,
                    wait_for_commit=False,
                )
            except Exception:
                Session.rollback()
                logging.exception(
                    "Could not reconcile failed creation of workflow %s.",
                    workflow_uuid,
                )
        raise
    except Exception:
        try:
            _reconcile_failed_creation(
                workflow_uuid,
                user_id,
                workspace_path,
                compensate,
                wait_for_commit=True,
            )
        except Exception:
            Session.rollback()
            logging.exception(
                "Could not reconcile ambiguous creation of workflow %s.",
                workflow_uuid,
            )
        raise
