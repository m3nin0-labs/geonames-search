#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Query param module."""

from .base import ParamInterpreter


#
# Interpreter
#
class QueryStrParam(ParamInterpreter):
    """Query text parameter interpreter."""

    def apply(self, search, params):
        """Interpret query string."""
        q_str = params.get("q")

        # validating query string
        if q_str:
            query = self.config.query_parser_cls().parse(q_str)
            search = search.query(query)

        return search
