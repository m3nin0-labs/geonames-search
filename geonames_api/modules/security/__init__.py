#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Security module."""

from flask_cors import CORS

cors = CORS()


def init_module(app):
    """Initialize the ``Security`` module."""
    cors.init_app(app)


__all__ = ("init_module",)
