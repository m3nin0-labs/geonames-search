#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Service configuration module."""

from .parser import QueryParser
from .results import RecordList
from .schema import GeonamesRecordSchema
from .search import params


class SearchOptions:
    """Search options class."""

    query_parser_cls = QueryParser

    sort_default = "bestmatch"
    sort_default_no_query = "newest"
    sort_options = {
        "bestmatch": dict(title="Best match", fields=["_score"]),
        "newest": dict(title="Newest", fields=["-modification_date"]),
        "oldest": dict(title="Oldest", fields=["modification_date"]),
    }

    pagination_options = {"default_results_per_page": 25, "default_max_results": 10000}

    params_interpreters_cls = [
        params.QueryStrParam,
        params.PaginationParam,
        params.SortParam,
    ]


class GeonamesAPIServiceConfig:
    """Configuration for the Geonames service."""

    #
    # Common configuration
    #
    # result_item_cls = RecordItem
    result_list_cls = RecordList

    #
    # Search configuration.
    #
    search = SearchOptions

    #
    # Search index configurations
    #
    index = "geonames"

    #
    # Record schema
    #
    schema = GeonamesRecordSchema
