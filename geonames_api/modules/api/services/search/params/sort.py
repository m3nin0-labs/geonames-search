#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Sort param module."""

from marshmallow import ValidationError

from .base import ParamInterpreter


class SortParam(ParamInterpreter):
    """Interpret sort parameter.

    Note:
        This class was created based on ``Invenio Records Resources``.
    """

    def _default_sort(self, params, options):
        """Get default sort."""
        if params.get("q"):
            return self.config.sort_default
        else:
            return self.config.sort_default_no_query

    def _handle_empty_query(self, params, options):
        """Handle invalid options for empty query string."""
        if params["sort"] == "bestmatch":
            return self.config.sort_default_no_query
        else:
            return params["sort"]

    def apply(self, search, params):
        """Interpret the sort string."""
        options = self.config.sort_options

        if "sort" not in params:
            params["sort"] = self._default_sort(params, options)

        if not params.get("q"):
            params["sort"] = self._handle_empty_query(params, options)

        sort = options.get(params["sort"])

        if sort is None:
            raise ValidationError(f"Invalid sort option '{params['sort']}'")

        return search.sort(*sort["fields"])
