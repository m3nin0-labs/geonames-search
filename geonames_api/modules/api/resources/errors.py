#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Resources errors module."""


from flask_resources import HTTPJSONException


class HTTPJSONInternalError(HTTPJSONException):
    """HTTP exception for Internal errors."""

    description = "Internal server error"

    def __init__(self, exception):
        super().__init__(code=500)


class HTTPJSONValidationException(HTTPJSONException):
    """HTTP exception serialization to JSON where errors are in a list.

    Note:
        This code was adapted from ``Invenio-Records-Resources``.
    """

    description = "A validation error occurred."

    def __init__(self, exception):
        super().__init__(code=400, errors=exception.messages)
