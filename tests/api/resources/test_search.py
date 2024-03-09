#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Search endpoint module."""


def test_search(test_client):
    """Test search endpoint."""

    response = test_client.get("/geonames/")

    assert response.status_code == 200  # noqa
    assert len(response.json.keys()) > 0
