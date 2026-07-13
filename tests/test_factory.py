# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2018, 2020, 2021, 2024, 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Test factory app."""

from mock import patch

from reana_server.factory import create_minimal_app


@patch("reana_server.factory.initialise_workspace_umask")
def test_create_app(mock_initialise_workspace_umask):
    """Test create_minimal_app() method."""
    create_minimal_app()

    mock_initialise_workspace_umask.assert_called_once_with()
