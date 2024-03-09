#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API API module."""

from werkzeug.exceptions import InternalServerError, NotFound

from .errors import error_json_response
from .resources.config import GeonamesAPIResourceConfig
from .resources.resource import GeonamesAPIResource
from .services.config import GeonamesAPIServiceConfig
from .services.service import GeonamesAPIService


def init_module(app):
    """Initialize the ``Rest API`` module."""

    # configurations
    service_config = GeonamesAPIServiceConfig()
    resource_config = GeonamesAPIResourceConfig()

    # service
    service = GeonamesAPIService(config=service_config)

    # resource
    resource = GeonamesAPIResource(config=resource_config, service=service)

    # registering blueprint
    app.register_blueprint(resource.as_blueprint())

    # general errors
    app.register_error_handler(NotFound, error_json_response)
    app.register_error_handler(InternalServerError, error_json_response)


__all__ = ("init_module",)
