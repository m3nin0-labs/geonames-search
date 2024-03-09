#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API configuration module."""

from dynaconf import FlaskDynaconf


def init_module(app):
    """Initialize the ``Configuration`` module."""
    FlaskDynaconf(app)


__all__ = ("init_module",)
