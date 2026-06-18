import { spawnSync } from "node:child_process";

function run(command, args) {
  const result = spawnSync(command, args, {
    stdio: "inherit",
  });

  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}

run("k3d", [
  "cluster",
  "create",
  "--config",
  "infra/kubernetes/k3d-cluster.yaml",
]);

run("kubectl", [
  "apply",
  "-f",
  "infra/kubernetes/manifests/sample-service.yaml",
]);

run("kubectl", [
  "wait",
  "--namespace",
  "toolshare-sample",
  "--for=condition=available",
  "deployment/sample-web",
  "--timeout=120s",
]);

console.log("Local Kubernetes cluster is ready.");
console.log('Sample service: curl.exe -H "Host: sample.toolshare.localhost" http://localhost:8088');
