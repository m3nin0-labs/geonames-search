#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Pagination base module."""


class Pagination:
    """Pagination helper class."""

    def __init__(self, size, page, max_results):
        """Initializer.

        Args:
            size (int): Number of results (int >= 1)

            page (int): Page number (int >= 1)

            max_results (int): Max number of results (int >= 1)

        See:
            This class was created based on ``Invenio-records-resources`` code.
        """
        self.size = size
        self.page = page
        self.max_results = max_results

    def valid(self):
        """Check if the pagination definition is valid."""
        pre_condition = 1 <= self.size and 1 <= self.page
        return pre_condition and 0 <= self.from_idx < self.max_results

    @property
    def from_idx(self):
        """Start index (with respect to all results) for this page."""
        return (self.page - 1) * self.size

    @property
    def to_idx(self):
        """Stop index (with respect to all results) for this page.

        Note:
            This valus is not inclusive (n - 1).
        """
        return min(self.page * self.size, self.max_results)
