#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API modules."""

from importlib import import_module

MODULES = [
    "geonames_api.modules.config",
    "geonames_api.modules.schema",
    "geonames_api.modules.api",
    "geonames_api.modules.cache",
    "geonames_api.modules.security",
]


def init_modules(app):
    """Initialize extension modules using the Application Module approach."""

    for module in MODULES:
        mod = import_module(module)
        mod.init_module(app)
