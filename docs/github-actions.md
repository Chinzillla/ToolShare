# GitHub Actions

The root workflow is defined in:

```text
.github/workflows/service-templates.yml
```

It runs automatically for pushes and pull requests. You can also test jobs
locally with [`act`](https://nektosact.com/).

## Local Requirements

- Docker Desktop is running.
- `act` is installed and available in the terminal.

List the workflow jobs:

```powershell
act -W .github/workflows/service-templates.yml -l
```

## Run the Media Service Job

From the repository root:

```powershell
act pull_request -W .github/workflows/service-templates.yml -j media-service -P ubuntu-24.04=ghcr.io/catthehacker/ubuntu:full-24.04 --container-options "--user 0"
```

The platform mapping is required because `act` does not automatically map the
`ubuntu-24.04` GitHub runner. The root user option allows the local runner
container to access Docker Desktop through the mounted Docker socket. These
options are only needed for local `act` execution.

The first run downloads the runner image and can take several minutes.

## Run Another Job

Replace `media-service` with the desired job ID:

```powershell
act pull_request -W .github/workflows/service-templates.yml -j <job-id> -P ubuntu-24.04=ghcr.io/catthehacker/ubuntu:full-24.04 --container-options "--user 0"
```

Current job IDs:

- `nestjs-template`
- `fastapi-template`
- `media-service`
- `database-infrastructure`
