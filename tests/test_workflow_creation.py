# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Tests for reconciliation of ambiguous controller creation failures."""

from unittest.mock import Mock, patch

import pytest
from bravado.exception import BravadoConnectionError, BravadoTimeoutError, HTTPError

from reana_server import workflow_creation
from reana_server.workflow_creation import create_workflow_on_controller


@pytest.mark.parametrize(
    "error, wait_for_commit",
    [
        (HTTPError(Mock(status_code=500)), False),
        (BravadoTimeoutError(), True),
        (BravadoConnectionError(), True),
        (ValueError("truncated controller response"), True),
    ],
)
def test_ambiguous_controller_failure_is_compensated(error, wait_for_commit):
    """Visible controller commits are compensated before the error escapes."""
    workflow = Mock(workspace_path="/workspaces/reserved")
    compensate = Mock()

    with patch(
        "reana_server.workflow_creation._find_created_workflow",
        return_value=workflow,
    ), patch(
        "reana_server.workflow_creation._reconcile_failed_creation",
        wraps=workflow_creation._reconcile_failed_creation,
    ) as reconcile:
        with pytest.raises(type(error)):
            create_workflow_on_controller(
                Mock(side_effect=error),
                "reserved",
                "owner",
                "/workspaces/reserved",
                compensate,
            )

    compensate.assert_called_once_with(workflow)
    assert reconcile.call_args.kwargs["wait_for_commit"] is wait_for_commit


def test_controller_4xx_is_not_compensated():
    """A definitive rejected request does not trigger creation reconciliation."""
    error = HTTPError(Mock(status_code=400))
    with patch(
        "reana_server.workflow_creation._reconcile_failed_creation"
    ) as reconcile:
        with pytest.raises(HTTPError):
            create_workflow_on_controller(
                Mock(side_effect=error),
                "reserved",
                "owner",
                "/workspaces/reserved",
                Mock(),
            )
    reconcile.assert_not_called()


@pytest.mark.parametrize(
    "error",
    [
        BravadoTimeoutError(),
        BravadoConnectionError(),
        ValueError("truncated controller response"),
    ],
)
def test_non_http_failure_reconciles_persisted_reserved_workflow(
    error, sample_serial_workflow_in_db, user0
):
    """An ambiguous failure after controller commit finds the reserved row."""
    compensate = Mock()

    with pytest.raises(type(error)):
        create_workflow_on_controller(
            Mock(side_effect=error),
            sample_serial_workflow_in_db.id_,
            user0.id_,
            sample_serial_workflow_in_db.workspace_path,
            compensate,
        )

    compensate.assert_called_once_with(sample_serial_workflow_in_db)
