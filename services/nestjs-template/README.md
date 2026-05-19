# nestjs-template

This directory is a reusable NestJS service template for TypeScript services.

## Environment

Copy `.env.example` when you need local environment values.

```env
NODE_ENV=development
PORT=3000
LOG_LEVEL=info
```

| Name | Default | Allowed values |
| --- | --- | --- |
| `NODE_ENV` | `development` | `development`, `test`, `production` |
| `PORT` | `3000` | Positive integer |
| `LOG_LEVEL` | `info` | `fatal`, `error`, `warn`, `info`, `debug`, `trace` |

## Local Development

Run commands from the repository root.

```bash
pnpm --filter @toolshare/nestjs-template start:dev
```

Health check:

```bash
curl http://localhost:3000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "nestjs-template",
  "uptime": 1.23,
  "timestamp": "2026-05-17T00:00:00.000Z"
}
```

## Checks

```bash
pnpm --filter @toolshare/nestjs-template test
pnpm --filter @toolshare/nestjs-template build
pnpm --filter @toolshare/nestjs-template test:e2e
```

## Docker

Build the image from the repository root:

```bash
docker build -f services/nestjs-template/Dockerfile -t toolshare-nestjs-template services/nestjs-template
```

Run the container:

```bash
docker run --rm -p 3000:3000 toolshare-nestjs-template
```

Then visit:

```text
http://localhost:3000/health
```

## Creating A New Service From This Template

1. Copy the template nestjs-template folder and rename it to the service you want to use
2. Search and replace nestjs-template to your service name
3. Keep the health route, config validation, structured logging, graceful shutdown, and tests.
