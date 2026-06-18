# Search Service

FastAPI service for connecting ToolShare to local OpenSearch. This service currently proves OpenSearch connectivity and exposes infrastructure health endpoints. Search business logic is intentionally not implemented yet.

## Local Setup

Start OpenSearch and create the local index from the repository root:

```shell
docker compose -f infra/docker-compose.yml up -d opensearch opensearch-dashboards
corepack pnpm search:index:bootstrap
```

Create and install the Python environment:

```shell
cd services/search-service
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Run the service:

```shell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/health
http://localhost:8000/search/health
http://localhost:8000/docs
```

## Configuration

The service validates required configuration at startup.

| Variable | Description | Local example |
| --- | --- | --- |
| `SERVICE_NAME` | Service name used in logs and health responses | `search-service` |
| `ENVIRONMENT` | `development`, `test`, or `production` | `development` |
| `PORT` | HTTP server port | `8000` |
| `LOG_LEVEL` | Python logging level | `INFO` |
| `OPENSEARCH_URL` | OpenSearch API URL | `https://localhost:9200` |
| `OPENSEARCH_USERNAME` | OpenSearch username | `admin` |
| `OPENSEARCH_PASSWORD` | OpenSearch password | Local development value |
| `OPENSEARCH_INDEX_EQUIPMENT_LISTINGS` | Equipment listing search index | `equipment-listings` |
| `OPENSEARCH_VERIFY_CERTS` | Whether to verify TLS certificates | `false` |

Use `.env.example` for local development only. Production credentials must come from the deployment environment or a secrets manager.

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/health` | Service health check |
| `GET` | `/search/health` | OpenSearch cluster health through the service |
| `GET` | `/docs` | Local OpenAPI documentation |

## Tests

From `services/search-service`:

```shell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m pytest -m "not integration"
```

Run the OpenSearch integration tests while local OpenSearch is running:

```shell
.\.venv\Scripts\python.exe -m pytest -m integration
```

Use `python -m pytest` through the service virtual environment so tests run with the intended interpreter and dependencies.

## Docker

Build from the repository root:

```shell
docker build -f services/search-service/Dockerfile -t toolshare-search-service services/search-service
```

On Docker Desktop, run the container against OpenSearch running on the host:

```shell
docker run --rm -p 8000:8000 --env-file services/search-service/.env.example -e OPENSEARCH_URL=https://host.docker.internal:9200 toolshare-search-service
```

On Linux, also map the host gateway:

```shell
docker run --rm -p 8000:8000 --add-host=host.docker.internal:host-gateway --env-file services/search-service/.env.example -e OPENSEARCH_URL=https://host.docker.internal:9200 toolshare-search-service
```

The image runs as a non-root user. Its service health endpoint is `/health`.

## Current Scope

Implemented:

- OpenSearch configuration validation
- OpenSearch client creation
- OpenSearch cluster health route
- Local index bootstrap command

Not implemented yet:

- Equipment indexing workflows
- Search query API
- Ranking, filters, pagination, or autocomplete
