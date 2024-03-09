#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API module."""

from flask import Flask

from geonames_api.modules import init_modules


def create_app():
    """Create Geonames API."""

    #
    # Creating app
    #
    app = Flask(__name__)

    #
    # Loading extensions
    #
    init_modules(app)

    return app


__version__ = "0.1.0"

__all__ = (
    "__version__",
    "create_app",
)
