# Local Infrastructure

This Compose stack starts the local infrastructure dependencies used by ToolShare development.

## Start

```shell
docker compose -f infra/docker-compose.yml up -d
```

## Stop

```shell
docker compose -f infra/docker-compose.yml down
```

## Reset

This removes containers and local volumes.

```shell
docker compose -f infra/docker-compose.yml down -v
```

## Services

| Service | Purpose | Local URL / Port |
|---|---|---|
| PostgreSQL | Relational database | `localhost:5432` |
| Redis | Cache and lightweight queues | `localhost:6379` |
| Redpanda | Kafka-compatible broker | `localhost:9092` |
| Redpanda Console | Broker UI | `http://localhost:8080` |
| OpenSearch | Search API | `https://localhost:9200` |
| OpenSearch Dashboards | Search UI | `http://localhost:5601` |
| MinIO | S3-compatible object storage | `http://localhost:9000` |
| MinIO Console | Object storage UI | `http://localhost:9001` |
| Temporal | Workflow engine frontend | `localhost:7233` |
| Temporal UI | Workflow UI | `http://localhost:8233` |
| Mailpit SMTP | Local SMTP server | `localhost:1025` |
| Mailpit UI | Local email inbox | `http://localhost:8025` |

## Service Databases

| Service | Database | Owner |
|---|---|---|
| User | `toolshare_user_db` | `toolshare_user_service` |
| Catalog | `toolshare_catalog_db` | `toolshare_catalog_service` |
| Booking | `toolshare_booking_db` | `toolshare_booking_service` |
| Payment | `toolshare_payment_db` | `toolshare_payment_service` |
| Review | `toolshare_review_db` | `toolshare_review_service` |
| Notification | `toolshare_notification_db` | `toolshare_notification_service` |
| Admin | `toolshare_admin_db` | `toolshare_admin_service` |
| Risk | `toolshare_risk_db` | `toolshare_risk_service` |

Each service owns and connects only to its own database.

## Database Commands

Reset all local service databases:

```shell
pnpm db:reset --yes
```

## Local Credentials

These credentials are for local development only. Do not reuse them in deployed environments.

| Service | Username | Password |
|---|---|---|
| PostgreSQL | `toolshare` | `toolshare` |
| OpenSearch Dashboards | `admin` | `ToolshareLocal123!` |
| MinIO Console | `toolshare` | `toolshare-local-minio` |

## Health Checks

Check container health:

```shell
docker compose -f infra/docker-compose.yml ps
```

Check MinIO:

```shell
curl.exe -i http://localhost:9000/minio/health/live
```

### OpenSearch

#### Validate OpenSearch locally:

```shell
docker compose -f infra/docker-compose.yml up -d opensearch opensearch-dashboards
docker compose -f infra/docker-compose.yml ps opensearch opensearch-dashboards
curl.exe --insecure --user admin:ToolshareLocal123! https://localhost:9200/_cluster/health
```

### Temporal Sample Worker

#### Validate Temporal locally:

```shell
corepack pnpm --filter @toolshare/temporal-sample-worker typecheck
docker compose -f infra/docker-compose.yml up -d temporal
docker exec toolshare-temporal temporal operator namespace list --address localhost:7233
```

Local Temporal uses the `default` namespace and the `booking-local` task queue.

#### Start the worker from the repository root:

```shell
corepack pnpm --filter @toolshare/temporal-sample-worker worker
```

In another terminal, start a sample workflow:

```shell
corepack pnpm --filter @toolshare/temporal-sample-worker start:workflow
```

Open the Temporal UI:
```shell
http://localhost:8233
```