# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Tests for the REANA Flask extension (security headers and CORS)."""

import pytest
from flask import Flask
from invenio_rest import InvenioREST
from mock import patch
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import UnprocessableEntity

_TEST_ORIGIN = "https://example.com:30443"

_EXPECTED_SECURITY_HEADERS = {
    "Cross-Origin-Opener-Policy": "same-origin",
    "Cross-Origin-Resource-Policy": "same-origin",
    "Cache-Control": "no-store",
}


@pytest.fixture
def ext_app():
    """Minimal Flask app with the REANA extension and CORS enabled."""
    from reana_server.ext import REANA

    app = Flask(__name__)
    app.config.update(
        {
            "TESTING": True,
            "SECRET_KEY": "test-secret",
            "REST_ENABLE_CORS": True,
            "REST_CSRF_ENABLED": False,
            "CORS_ORIGINS": [_TEST_ORIGIN],
            "CORS_SEND_WILDCARD": False,
            "CORS_SUPPORTS_CREDENTIALS": False,
        }
    )

    @app.route("/test")
    def test_route():
        return "OK"

    InvenioREST(app)
    REANA().init_app(app)
    return app


@patch("reana_server.ext.initialise_workspace_umask")
def test_initialise_workspace_umask(mock_initialise_workspace_umask):
    """Initialise the workspace umask when loading the full extension."""
    from reana_server.ext import REANA

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "test-secret"

    REANA().init_app(app)

    mock_initialise_workspace_umask.assert_called_once_with()


@pytest.mark.parametrize("header,value", _EXPECTED_SECURITY_HEADERS.items())
def test_security_headers_on_normal_response(ext_app, header, value):
    """Each security header is set to the expected value on every response."""
    with ext_app.test_client() as client:
        res = client.get("/test")
    assert res.headers.get(header) == value


def test_permissions_policy_present(ext_app):
    """Permissions-Policy header is present on every response."""
    with ext_app.test_client() as client:
        res = client.get("/test")
    assert "Permissions-Policy" in res.headers


def test_cors_matching_origin_echoed_back(ext_app):
    """A request from the allowed origin gets Access-Control-Allow-Origin echoed."""
    with ext_app.test_client() as client:
        res = client.get("/test", headers={"Origin": _TEST_ORIGIN})
    assert res.headers.get("Access-Control-Allow-Origin") == _TEST_ORIGIN


def test_cors_non_matching_origin_rejected(ext_app):
    """A request from a different origin does not get Access-Control-Allow-Origin."""
    with ext_app.test_client() as client:
        res = client.get("/test", headers={"Origin": "https://example.com"})
    assert "Access-Control-Allow-Origin" not in res.headers


def _render_args_validation_error(app, messages):
    """Return the message an argument-validation failure would produce."""
    from reana_server.ext import handle_args_validation_error

    error = UnprocessableEntity()
    error.exc = ValidationError(messages)
    with app.test_request_context():
        response, status_code = handle_args_validation_error(error)
    return response.get_json()["message"], status_code


def test_nested_argument_errors_render_the_actual_complaint(ext_app):
    """Webargs namespaces messages per location; the leaf message must survive."""
    message, status_code = _render_args_validation_error(
        ext_app, {"json": {"reana_specification": ["Unknown field."]}}
    )

    assert status_code == 400
    # Joining the nested dict directly used to render its keys instead, i.e.
    # "Field 'json': reana_specification".
    assert message == "Field 'reana_specification': Unknown field."


def test_deeply_nested_argument_errors_keep_their_field_path(ext_app):
    """Nested schemas and collections keep an unambiguous field path."""
    message, _status_code = _render_args_validation_error(
        ext_app, {"json": {"input_parameters": {"nested": ["Not a valid integer."]}}}
    )

    assert message == "Field 'input_parameters.nested': Not a valid integer."


def test_multiple_argument_errors_are_all_reported(ext_app):
    """Every failing field is reported, not just the first one."""
    message, _status_code = _render_args_validation_error(
        ext_app,
        {
            "query": {
                "status": ["Missing data for required field."],
                "size": ["Not a valid integer."],
            }
        },
    )

    assert "Field 'status': Missing data for required field." in message
    assert "Field 'size': Not a valid integer." in message
