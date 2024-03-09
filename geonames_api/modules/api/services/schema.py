#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Services schema module."""

from marshmallow import Schema, exceptions, fields


#
# Utilities
#
class SchemaWrapper:
    """Interface to manage a schema in a service."""

    _schema = None
    """Model schema."""

    def __init__(self, schema):
        """Initializer."""
        # can be used to include a permission checker
        # (e.g., avoid some fields to be presented).
        self._schema = schema

    #
    # High-level methods
    #
    def validate(self, data: dict, raise_exception: bool = True) -> bool:
        """Validate a data based on a schema."""
        validation_result = self._schema().validate(data)

        has_errors = len(validation_result.keys()) > 0

        if has_errors and raise_exception:
            raise exceptions.ValidationError(validation_result)

        return has_errors

    def dump(self, data, schema_args=None, context=None):
        """Dump data."""
        schema_args = schema_args or {}
        base_context = context or {}

        return self._schema(context=base_context, **schema_args).dump(data)


#
# Record schemas
#
class GeonamesRecordSchema(Schema):
    """Geonames record schema."""

    geonameid = fields.Str()

    name = fields.Str()

    asciiname = fields.Str()

    alternativenames = fields.List(fields.Str)

    # ToDo: Check the correct name
    coordinates = fields.Str()

    feature_class = fields.Str()

    feature_code = fields.Str()

    country_code3 = fields.Str()

    admin1_code = fields.Str()

    admin2_code = fields.Str()

    admin3_code = fields.Str()

    admin4_code = fields.Str()

    # ToDo: Review this type
    population = fields.Str()

    alt_name_length = fields.Int()

    modication_date = fields.Date()
