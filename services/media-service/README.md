# Media Service

FastAPI service for managing ToolShare media storage. Files are stored in private
MinIO buckets and accessed through time-limited signed URLs.

## Buckets

| Bucket | Purpose |
| --- | --- |
| `equipment-photos` | Equipment listing photos |
| `pickup-photos` | Equipment condition at pickup |
| `return-photos` | Equipment condition at return |
| `dispute-evidence` | Evidence attached to disputes |

The local infrastructure bootstrap creates these buckets and disables anonymous
access.

## Local Setup

Start MinIO and create the required buckets from the repository root:

```bash
docker compose -f infra/docker-compose.yml up -d --build minio
docker compose -f infra/docker-compose.yml run --rm minio-bootstrap
```

Configure and start the service:

```bash
cd services/media-service
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
Copy-Item .env.example .env
python -m pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```

On macOS or Linux:

```bash
source .venv/bin/activate
cp .env.example .env
python -m pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```

Open:

- Health check: <http://localhost:8000/health>
- OpenAPI documentation: <http://localhost:8000/docs>
- OpenAPI schema: <http://localhost:8000/openapi.json>
- MinIO console: <http://localhost:9001>

## Configuration

The service validates all configuration at startup. Missing or invalid values
cause a clear startup failure.

| Variable | Description | Local example |
| --- | --- | --- |
| `SERVICE_NAME` | Service name used in logs and health responses | `media-service` |
| `ENVIRONMENT` | `development`, `test`, or `production` | `development` |
| `PORT` | HTTP server port | `8000` |
| `LOG_LEVEL` | Python logging level | `INFO` |
| `MINIO_ENDPOINT` | MinIO host and port without a URL scheme | `localhost:9000` |
| `MINIO_ACCESS_KEY` | MinIO access key | `toolshare` |
| `MINIO_SECRET_KEY` | MinIO secret key | Local development value |
| `MINIO_USE_SSL` | Whether the MinIO connection uses TLS | `false` |
| `MINIO_EQUIPMENT_PHOTOS_BUCKET` | Equipment photo bucket | `equipment-photos` |
| `MINIO_PICKUP_PHOTOS_BUCKET` | Pickup photo bucket | `pickup-photos` |
| `MINIO_RETURN_PHOTOS_BUCKET` | Return photo bucket | `return-photos` |
| `MINIO_DISPUTE_EVIDENCE_BUCKET` | Dispute evidence bucket | `dispute-evidence` |
| `MINIO_SIGNED_URL_EXPIRY_SECONDS` | Signed URL lifetime from 60 to 3600 seconds | `900` |

Use `.env.example` for local development only. Production credentials must come
from the deployment environment or a secrets manager.

## Storage Access

Buckets remain private. The storage client creates time-limited signed upload
and download URLs so clients do not receive MinIO credentials or permanent
public access.

## Quality Checks

From `services/media-service`:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -m "not integration"
```

Run the MinIO integration test while the local infrastructure is running:

```bash
python -m pytest -m integration
```

The integration test verifies authenticated object upload, denied anonymous
access, and successful access through a signed URL.

## Docker

Build from the repository root:

```bash
docker build -f services/media-service/Dockerfile -t toolshare-media-service services/media-service
```

On Docker Desktop, run the container against MinIO running on the host:

```bash
docker run --rm -p 8000:8000 --env-file services/media-service/.env.example -e MINIO_ENDPOINT=host.docker.internal:9000 toolshare-media-service
```

On Linux, also map the host gateway:

```bash
docker run --rm -p 8000:8000 --add-host=host.docker.internal:host-gateway --env-file services/media-service/.env.example -e MINIO_ENDPOINT=host.docker.internal:9000 toolshare-media-service
```

The image runs as a non-root user. Its health check endpoint is `/health`.
