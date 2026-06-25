# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017, 2018, 2020, 2021, 2026 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Reana-Server Ping-functionality Flask-Blueprint."""

from flask import Blueprint, jsonify

from reana_server import __version__
from reana_server.config import REANA_API_CAPABILITIES

blueprint = Blueprint("ping", __name__)


@blueprint.route("/ping", methods=["GET"])
def ping():  # noqa
    r"""Endpoint to ping the server. Responds with a pong.
    ---
    get:
      summary: Ping the server (healthcheck)
      operationId: ping
      description: >-
        Ping the server.


        This endpoint is deliberately unauthenticated: it also carries the
        protocol bootstrap signal that a client needs *before* it authenticates
        or builds a request body. ``api_capabilities`` advertises the
        client-facing protocols the server implements; a released server omits
        the field, which identifies it as legacy.
      produces:
       - application/json
      responses:
        200:
          description: >-
            Ping succeeded. Service is running and accessible.
          schema:
            type: object
            properties:
              message:
                type: string
              status:
                type: string
              reana_server_version:
                type: string
              api_capabilities:
                description: >-
                  Client-facing protocols implemented by this server. Absent on
                  released servers that predate protocol negotiation.
                type: array
                items:
                  type: string
          examples:
            application/json:
              message: OK
              status: 200
              reana_server_version: 0.95.0a6
              api_capabilities: ["workflow-specification-bundles-v1"]
    """

    return (
        jsonify(
            message="OK",
            status="200",
            reana_server_version=__version__,
            api_capabilities=REANA_API_CAPABILITIES,
        ),
        200,
    )
