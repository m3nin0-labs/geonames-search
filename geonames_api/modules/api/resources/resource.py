#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Resource module."""

from flask_resources import (
    from_conf,
    request_parser,
    resource_requestctx,
    response_handler,
    route,
)

from ...cache import cache
from .base import Resource

#
# Decorators
#
request_search_args = request_parser(from_conf("request_search_args"), location="args")


#
# Resources
#
class GeonamesAPIResource(Resource):
    """Resource of Geonames API."""

    #
    # Routes configuration
    #
    def create_url_rules(self):
        """Create URL rules."""
        return [route("GET", "/", self.search)]

    #
    # Search
    #
    @request_search_args
    @response_handler(many=True)
    @cache.cached(query_string=True)
    def search(self):
        """Search Geonames records."""
        hits = self.service.search(params=resource_requestctx.args)

        return hits.to_dict(), 200
