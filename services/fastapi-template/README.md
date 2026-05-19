# FastAPI Service Template

This directory is a reusable FastAPI template for Python services

## Environment

```env
SERVICE_NAME=fastapi-template
ENVIRONMENT=development
PORT=8000
LOG_LEVEL=INFO
```

Valid `ENVIRONMENT` values are `development`, `test`, and `production`.

Valid `LOG_LEVEL` values are `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.

## Local Development

From `services/fastapi-template`:

```bash
python -m venv .venv
.venv/Scripts/activate
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

From `services/fastapi-template`:

```bash
python -m pytest
```

## Docker

From the repository root:

```bash
docker build -f services/fastapi-template/Dockerfile -t toolshare-fastapi-template services/fastapi-template
docker run --rm -p 8000:8000 toolshare-fastapi-template
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

1. Copy `services/fastapi-template` to `services/<service-name>`.
2. Inside the copied folder, search for `fastapi-template` and replace it with `<service-name>`.
3. Keep health checks, config validation, structured logging, tests, and Docker support.
4. Add service-specific routes and business logic only in the copied service.
