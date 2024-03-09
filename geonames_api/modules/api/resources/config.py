#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Resource configuration module."""

import opensearchpy
from flask_resources import (
    JSONDeserializer,
    JSONSerializer,
    RequestBodyParser,
    ResponseHandler,
    create_error_handler,
)
from flask_resources import (
    ResourceConfig as BaseResourceConfig,
)
from marshmallow import ValidationError

from .args import SearchRequestArgsSchema
from .errors import HTTPJSONInternalError, HTTPJSONValidationException


class GeonamesAPIResourceConfig(BaseResourceConfig):
    """Configuration for the Geonames API Resource."""

    #
    # Blueprint
    #
    blueprint_name = "geonames_api_resource"

    #
    # Address
    #
    url_prefix = "/geonames"

    #
    # Request
    #
    # (ToDo) request_view_args = something
    request_search_args = SearchRequestArgsSchema

    #
    # Body
    #
    request_body_parsers = {"application/json": RequestBodyParser(JSONDeserializer())}

    #
    # Serializers
    #
    response_handlers = {"application/json": ResponseHandler(JSONSerializer())}

    #
    # Errors
    #
    error_handlers = {
        ValidationError: create_error_handler(lambda e: HTTPJSONValidationException(e)),
        opensearchpy.exceptions.ConnectionError: create_error_handler(
            lambda e: HTTPJSONInternalError(e)
        ),
    }
