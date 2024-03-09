#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Resources base module."""

from flask_resources import Resource as BaseResource


class Resource(BaseResource):
    """Base resource class Geonames API."""

    _service = None
    """Resource service."""

    def __init__(self, config, service):
        """Initializer."""

        self._service = service
        super().__init__(config)

    @property
    def service(self):
        """Service attribute."""
        return self._service
