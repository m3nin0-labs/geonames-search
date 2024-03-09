#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Service results module."""

from .search.pagination import Pagination


class ServiceResult:
    """Base service result class."""


class RecordList(ServiceResult):
    """Record list result class."""

    def __init__(
        self,
        service,
        results,
        params=None,
        links_tpl=None,
        links_item_tpl=None,
        schema=None,
    ):
        self._service = service
        self._results = results
        self._schema = schema or service.schema
        self._params = params
        self._links_tpl = links_tpl
        self._links_item_tpl = links_item_tpl

    #
    # Base methods
    #
    def __len__(self):
        """Return the number of hits."""
        return self.total

    def __iter__(self):
        """Hits iterator."""
        return self.hits

    #
    # Properties
    #
    @property
    def total(self):
        """Total number of hits."""
        if hasattr(self._results, "hits"):
            return self._results.hits.total["value"]
        return None

    @property
    def aggregations(self):
        """Get search results aggregations."""
        try:
            return self._results.labelled_facets.to_dict()

        except AttributeError:
            return None

    @property
    def hits(self):
        """Hits iterator."""
        for hit in self._results:
            record = hit.to_dict()

            # Project record
            projection = self._schema.dump(record, context=dict(record=record))

            if self._links_item_tpl:
                projection["links"] = self._links_item_tpl.expand(record)

            yield projection

    @property
    def pagination(self):
        """Content pagination."""
        return Pagination(self._params["size"], self._params["page"], self.total)

    def to_dict(self):
        """Object as dict."""
        res = {"hits": {"hits": list(self.hits), "total": self.total}}

        # ToDo: To be included
        # if self.aggregations:
        #     res["aggregations"] = self.aggregations

        # ToDo: To be included
        # if self._params:
        #     res["sortBy"] = self._params["sort"]
        #     if self._links_tpl:
        #         res["links"] = self._links_tpl.expand(self.pagination)

        return res
