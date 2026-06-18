# GitHub Actions

The root workflows are defined in:

```text
.github/workflows/service-templates.yml
.github/workflows/media-service.yml
.github/workflows/search-service.yml
.github/workflows/local-infrastructure.yml
```

They run automatically for pushes and pull requests. You can also test jobs
locally with [`act`](https://nektosact.com/).

## Local Requirements

- Docker Desktop is running.
- `act` is installed and available in the terminal.

List the workflow jobs:

```powershell
act -W .github/workflows/service-templates.yml -l
act -W .github/workflows/media-service.yml -l
act -W .github/workflows/search-service.yml -l
act -W .github/workflows/local-infrastructure.yml -l
```

## Run the Media Service Job

From the repository root:

```powershell
act pull_request -W .github/workflows/media-service.yml -j media-service -P ubuntu-24.04=ghcr.io/catthehacker/ubuntu:full-24.04 --container-options "--user 0"
```

The platform mapping is required because `act` does not automatically map the
`ubuntu-24.04` GitHub runner. The root user option allows the local runner
container to access Docker Desktop through the mounted Docker socket. These
options are only needed for local `act` execution.

The first run downloads the runner image and can take several minutes.

## Run the Search Service Job

From the repository root:

```powershell
act pull_request -W .github/workflows/search-service.yml -j search-service -P ubuntu-24.04=ghcr.io/catthehacker/ubuntu:full-24.04 --container-options "--user 0"
```

## Run Another Job

Use the workflow file and job ID for the check you want:

```powershell
act pull_request -W .github/workflows/<workflow-file>.yml -j <job-id> -P ubuntu-24.04=ghcr.io/catthehacker/ubuntu:full-24.04 --container-options "--user 0"
```

Current job IDs:

- `.github/workflows/service-templates.yml`: `nestjs-template`, `fastapi-template`
- `.github/workflows/media-service.yml`: `media-service`
- `.github/workflows/search-service.yml`: `search-service`
- `.github/workflows/local-infrastructure.yml`: `database-infrastructure`
