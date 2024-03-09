#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Service module."""

from .base import Service
from .search import index


class GeonamesAPIService(Service):
    """Geonames API Service."""

    def search(self, params):
        """Search geonames records."""
        search = index.create_search(self.config.index)

        # args evaluator
        search_opts = self.config.search

        for interpreter_cls in search_opts.params_interpreters_cls:
            search = interpreter_cls(search_opts).apply(search, params)

        # extras
        extras = {}
        extras["track_total_hits"] = True

        search = search.extra(**extras)

        # executing search
        search_result = search.execute()

        # projecting results and returning them
        return self.result_list(self, search_result, params)
