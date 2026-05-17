# ToolShare NestJS Service Template

This directory is a reusable NestJS service template for ToolShare TypeScript services, including the future API Gateway. Copy this template when creating a new backend service, then rename the package and update service-specific details.

The template intentionally contains no ToolShare business logic.

## Included

- `GET /health` health endpoint
- Zod environment validation
- Structured JSON logging with `nestjs-pino`
- Graceful shutdown hooks
- Jest unit test scaffold
- Docker build support
- Exact dependency versions for repeatable installs

## Environment

The service validates these environment variables at startup:

| Name | Default | Allowed values |
| --- | --- | --- |
| `NODE_ENV` | `development` | `development`, `test`, `production` |
| `PORT` | `3000` | Positive integer |
| `LOG_LEVEL` | `info` | `fatal`, `error`, `warn`, `info`, `debug`, `trace` |

Invalid values fail fast during startup.

## Local Development

Run commands from the repository root.

```bash
pnpm --filter @toolshare/service-template start:dev
```

Health check:

```bash
curl http://localhost:3000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "service-template",
  "uptime": 1.23,
  "timestamp": "2026-05-17T00:00:00.000Z"
}
```

## Checks

```bash
pnpm --filter @toolshare/service-template test
pnpm --filter @toolshare/service-template build
pnpm --filter @toolshare/service-template test:e2e
```

## Docker

Build the image from the repository root:

```bash
docker build -f services/template/Dockerfile -t toolshare-service-template .
```

Run the container:

```bash
docker run --rm -p 3000:3000 toolshare-service-template
```

Then visit:

```text
http://localhost:3000/health
```

## Creating A New Service From This Template

1. Copy `services/template` to `services/<service-name>`.
2. Rename the package in the copied `package.json`.
3. Update the `service` value returned by the health service.
4. Update Docker image names and filter commands for the new package.
5. Add service-specific modules, controllers, and providers.
6. Keep the health route, config validation, structured logging, graceful shutdown, and tests.

Do not add shared business logic to this template. Shared code should live in `packages/` when needed.
