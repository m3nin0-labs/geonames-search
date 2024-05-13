# Geonames Search

Geonames Search is a full-text search service for Geonames content, designed to facilitate the querying of geographical data through a simple and efficient interface. Built using Python, Flask, and Opensearch, this service provides a robust backend infrastructure leveraging Opensearch for data storage and full-text search capabilities, along with Redis for caching.

> **Note**: This is a hobby project.

## Features

- **Full-Text Search**: Quickly find geographical information using the full-text search capabilities of OpenSearch.
- **REST API**: Search Geonames content using the straightforward endpoint `/geonames?q=<query>`.
- **Scalable Infrastructure**: Built with Docker to ensure the service is easy to deploy and scale.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

- Git
- Make
- Python 3.9 or higher
- Poetry package management
- Docker and Docker Compose

### Installation (Docker)

1. **Clone the repository**

```bash
git clone https://github.com/m3nin0-labs/geonames-search.git

cd geonames-search
```

2. **Start the Infrastructure**

Use the `make up` command to start the OpenSearch instance, Redis cache, and the Geonames Search service.

```bash
make up
```

3. **Index Geonames**

To index the Geonames data, you can use the [Geonames Index project](https://github.com/m3nin0-labs/geonames-index).

## Development

1. **Clone the repository**

```bash
git clone https://github.com/m3nin0-labs/geonames-search.git

cd geonames-search
```

2. **Install Dependencies**

Install all necessary Python dependencies using Poetry.

```bash
poetry install --with dev
```

3. **Run the Application**

Start the Flask application.

```bash
FLASK_APP=geonames_api/main.py flask run
```

Now, you are ready to develop!

## Usage

To use the Geonames Search service, simply send a GET request to the endpoint with your search query:

```http
GET /geonames?q=London
```

Responses will include matched geographical data from the Geonames database.

## Contributing

We welcome contributions! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## License

`geonames-search` is distributed under the MIT license. See LICENSE for more details.
