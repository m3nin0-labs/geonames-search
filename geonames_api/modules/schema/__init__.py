#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API schema module."""

from flask_marshmallow import Marshmallow

ma = Marshmallow()


def init_module(app):
    """Initialize the ``Schema Validation`` module."""
    ma.init_app(app)


__all__ = (
    "ma",
    "init_module",
)
