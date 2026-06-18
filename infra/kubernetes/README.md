# Local Kubernetes

This setup is for deployment practice. It is separate from Docker Compose fast-dev mode.

## Requirements

- Docker Desktop
- kubectl
- k3d v5.9.0 or newer

## K8 Commands

From the repository root:

### Create Cluster

```shell
corepack pnpm k8s:create
```

This creates the `toolshare-k8` k3d cluster, uses the default Traefik ingress controller, and deploys the sample nginx service.

### Check Cluster

```shell
corepack pnpm k8s:check
```

### Check Nodes

```shell
corepack pnpm k8s:check-nodes
```

### Check Sample Service

```shell
kubectl get all -n toolshare-sample
kubectl get ingress -n toolshare-sample
curl.exe -H "Host: sample.toolshare.localhost" http://localhost:8088
```

The sample service should return the nginx welcome HTML.

### Delete Cluster

From the repository root:

```shell
corepack pnpm k8s:delete
```

## Files

- `infra/kubernetes/k3d-cluster.yaml`: local k3d cluster configuration.
- `infra/kubernetes/manifests/sample-service.yaml`: sample namespace, deployment, service, and ingress.
