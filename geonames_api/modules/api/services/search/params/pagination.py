#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Services Pagination param module."""

from ...errors import QueryStringValidationError
from ..pagination import Pagination
from .base import ParamInterpreter


class PaginationParam(ParamInterpreter):
    """Pagination interpreter."""

    def apply(self, search, params):
        """Interpret the pagination string."""
        options = self.config.pagination_options

        default_size = options["default_results_per_page"]

        params.setdefault("size", default_size)
        params.setdefault("page", 1)

        p = Pagination(params["size"], params["page"], options["default_max_results"])

        if not p.valid():
            return QueryStringValidationError("Invalid pagination parameters.")

        return search[p.from_idx : p.to_idx]
