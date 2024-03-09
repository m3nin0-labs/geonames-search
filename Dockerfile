#
# Copyright (C) 2023 Geonames API.
#
# Geonames API is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

FROM python:3.9

# Working directory
WORKDIR /app

# Copy application
COPY . .

# Install dependencies
RUN pip install --no-cache-dir .

# Base application
CMD ["gunicorn", "--bind", "0.0.0.0", "-w", "10", "geonames_api.main:app"]
