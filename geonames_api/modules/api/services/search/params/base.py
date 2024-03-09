#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Params base module."""


class ParamInterpreter:
    """Evaluate a URL parameter.

    Note:
        To learn more, check the Invenio Records Resources.
    """

    def __init__(self, config):
        """Initializer."""
        self.config = config

    def apply(self, search, params):
        """Apply parameters."""
        pass
