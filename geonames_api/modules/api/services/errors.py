#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Service errors module."""

from marshmallow import ValidationError


class QueryStringValidationError(ValidationError):
    """Error thrown when there is an issue with the Query string."""

    pass
