#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Service parser module."""

from luqum.exceptions import ParseError
from luqum.parser import parser as luqum_parser
from opensearchpy import Q


#
# Parser
#
class QueryParser:
    """Parse query string into a OpenSearch DSL Q object."""

    def parse(self, query_str: str):
        """Parse query."""
        try:
            luqum_parser.parse(query_str)
            return Q("query_string", query=query_str)
        except ParseError:
            return Q("multi_match", query=query_str)
