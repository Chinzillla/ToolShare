# FastAPI Service Template

This directory is a reusable FastAPI template for Python services

## Environment

```env
SERVICE_NAME=search-service
ENVIRONMENT=development
PORT=8000
LOG_LEVEL=INFO
```

Valid `ENVIRONMENT` values are `development`, `test`, and `production`.

Valid `LOG_LEVEL` values are `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

## Local Development

From `services/search-service`:

```bash
python -m venv .venv
.venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --port 8000
```

Open:

```text
http://localhost:8000/health
http://localhost:8000/docs
http://localhost:8000/openapi.json
```

## Tests

From `services/search-service`:

```bash
python -m pytest
```

## Docker

From the repository root:

```bash
docker build -f services/search-service/Dockerfile -t toolshare-search-service services/search-service
docker run --rm -p 8000:8000 toolshare-search-service
```

Health check path:

```text
/health
```

Then open:

```text
http://localhost:8000/health
http://localhost:8000/docs
```

## Creating A New Service From This Template

1. Copy `services/search-service` to `services/<service-name>`.
2. Inside the copied folder, search for `search-service` and replace it with `<service-name>`.
3. Keep health checks, config validation, structured logging, tests, and Docker support.
4. Add service-specific routes and business logic only in the copied service.
