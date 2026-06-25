# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Test the unauthenticated ping and protocol-capability contract."""

from flask import url_for

from reana_server import __version__
from reana_server.config import WORKFLOW_SPECIFICATION_BUNDLES_CAPABILITY


def test_ping_advertises_protocol_capabilities(base_app):
    """Ping stays unauthenticated and carries the protocol bootstrap signal."""
    with base_app.app_context(), base_app.test_client() as client:
        res = client.get(url_for("ping.ping"))

        assert res.status_code == 200
        payload = res.json
        # Released clients parse ``status`` as a string; keep it one.
        assert payload["message"] == "OK"
        assert payload["status"] == "200"
        assert payload["reana_server_version"] == __version__
        assert WORKFLOW_SPECIFICATION_BUNDLES_CAPABILITY in payload["api_capabilities"]
