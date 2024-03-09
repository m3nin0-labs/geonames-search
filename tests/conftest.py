#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Tests module."""

import pytest

from geonames_api import create_app


@pytest.fixture()
def test_app():
    """Flask application fixture."""

    app = create_app()

    yield app


@pytest.fixture()
def test_client(test_app):
    """Flask client fixture."""
    return test_app.test_client()
