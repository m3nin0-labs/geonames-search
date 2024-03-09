#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Service base module."""

from .schema import SchemaWrapper


class Service:
    """Base service class for Geonames API."""

    def __init__(self, config):
        """Initializer."""
        self._config = config

    @property
    def config(self):
        """Service configuration property."""
        return self._config

    @property
    def schema(self) -> SchemaWrapper:
        """Service schema property."""
        return SchemaWrapper(self._config.schema)

    def result_list(self, *args, **kwargs):
        """Create a new instance of the resource list."""
        return self.config.result_list_cls(*args, **kwargs)
