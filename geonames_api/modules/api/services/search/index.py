#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Geonames API Service base module."""


from flask import current_app
from opensearchpy import OpenSearch, Search


#
# Utilities
#
def create_search_client() -> OpenSearch:
    """Create an OpenSearch client.

    Note:
        To configure the client, please use the ``settings.toml`` file.
    """
    return OpenSearch(**current_app.config.opensearch.config)


def create_search(index: str) -> Search:
    """Create a ``opensearchpy.Search`` object.

    Args:
        index (str): Index name.

    Returns:
        Search: ``opensearchpy.Search`` object.
    """
    search_client = create_search_client()

    return Search(using=search_client, index=index)
