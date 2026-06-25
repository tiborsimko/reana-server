# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Tests for atomic workflow cloning."""

import copy
from unittest.mock import patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from reana_db.models import (
    RunStatus,
    Workflow,
    WorkspaceRetentionAuditLog,
    WorkspaceRetentionRule,
    WorkspaceRetentionRuleStatus,
)
from reana_server.utils import clone_workflow


@pytest.mark.parametrize(
    "failure,expected_exception,error_match",
    [
        (
            SQLAlchemyError("injected database failure"),
            RuntimeError,
            "Database connection failed",
        ),
        (
            ValueError("injected application failure"),
            ValueError,
            "injected application failure",
        ),
    ],
)
def test_clone_workflow_rolls_back_clone_and_retention_rules(
    app,
    monkeypatch,
    sample_serial_workflow_in_db,
    session,
    failure,
    expected_exception,
    error_match,
):
    """A retention failure must not persist a clone or change previous rules."""
    workflow = sample_serial_workflow_in_db
    retention_rules = [{"workspace_files": "**/*.root", "retention_days": 1}]
    workflow.set_workspace_retention_rules(retention_rules)
    workflow.activate_workspace_retention_rules()
    original_set_retention_rules = Workflow.set_workspace_retention_rules

    def fail_after_staging_retention_rules(cloned_workflow, rules, commit=True):
        original_set_retention_rules(cloned_workflow, rules, commit=commit)
        raise failure

    monkeypatch.setattr(
        Workflow,
        "set_workspace_retention_rules",
        fail_after_staging_retention_rules,
    )

    with pytest.raises(expected_exception, match=error_match):
        clone_workflow(workflow, None, None)

    session.expire_all()
    workflows = session.query(Workflow).filter_by(name=workflow.name).all()
    assert workflows == [workflow]
    assert [rule.status for rule in workflow.retention_rules] == [
        WorkspaceRetentionRuleStatus.active
    ]

    session.query(WorkspaceRetentionAuditLog).delete()
    session.query(WorkspaceRetentionRule).delete()
    session.commit()
    session.expire(workflow, ["retention_rules"])


def test_failed_restart_compensation_rolls_back_as_one_transaction(
    app, sample_serial_workflow_in_db, session, user0
):
    """A mid-compensation failure leaves clone and rule state untouched."""
    from reana_server.rest.workflows import _compensate_failed_restart

    workflow = sample_serial_workflow_in_db
    workflow.status = RunStatus.finished
    workflow.reana_specification = copy.deepcopy(workflow.reana_specification)
    workflow.reana_specification["workspace"] = {"retention_days": {"**/*.txt": 1}}
    session.commit()
    workflow.set_workspace_retention_rules(
        [{"workspace_files": "original.txt", "retention_days": 1}]
    )
    workflow.activate_workspace_retention_rules()
    prior_rule_states = {rule.id_: rule.status for rule in workflow.retention_rules}
    clone = clone_workflow(workflow, None, None)
    clone_id = clone.id_
    pre_compensation_status = clone.status
    assert pre_compensation_status != RunStatus.deleted
    pre_compensation_rule_states = {
        rule.id_: rule.status
        for rule in session.query(WorkspaceRetentionRule)
        .filter(WorkspaceRetentionRule.workflow_id.in_([workflow.id_, clone_id]))
        .all()
    }
    original_query = session.query

    def fail_after_bulk_status_update(*entities, **kwargs):
        if entities == (WorkspaceRetentionRule,):
            raise RuntimeError("injected retention restoration failure")
        return original_query(*entities, **kwargs)

    with patch.object(
        session, "query", side_effect=fail_after_bulk_status_update
    ), patch("reana_server.rest.workflows._recalculate_shared_workspace_quota"):
        _compensate_failed_restart(clone, prior_rule_states, user0)

    session.expire_all()
    persisted_clone = session.query(Workflow).filter_by(id_=clone_id).one()
    assert persisted_clone.status == pre_compensation_status
    assert {
        rule.id_: rule.status
        for rule in session.query(WorkspaceRetentionRule)
        .filter(WorkspaceRetentionRule.workflow_id.in_([workflow.id_, clone_id]))
        .all()
    } == pre_compensation_rule_states

    session.query(WorkspaceRetentionAuditLog).delete()
    session.query(WorkspaceRetentionRule).filter(
        WorkspaceRetentionRule.workflow_id.in_([workflow.id_, clone_id])
    ).delete(synchronize_session=False)
    session.delete(persisted_clone)
    session.commit()
    session.expire(workflow, ["retention_rules"])
