import { spawnSync } from "node:child_process";

function run(command, args) {
  const result = spawnSync(command, args, {
    stdio: "inherit",
  });

  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}

run("k3d", ["cluster", "delete", "toolshare-k8"]);

console.log("Local Kubernetes cluster deleted.");
