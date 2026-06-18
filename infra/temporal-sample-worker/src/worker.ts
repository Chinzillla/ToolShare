import { NativeConnection, Worker } from '@temporalio/worker';
import { fileURLToPath } from 'node:url';

import { temporalAddress, temporalNamespace, temporalTaskQueue } from './config.js';

const workflowsPath = fileURLToPath(new URL('./workflows.ts', import.meta.url));

async function run() {
  const connection = await NativeConnection.connect({
    address: temporalAddress,
  });

  try {
    const worker = await Worker.create({
      connection,
      namespace: temporalNamespace,
      taskQueue: temporalTaskQueue,
      workflowsPath,
    });

    console.log(
      `Temporal sample worker polling ${temporalTaskQueue} in namespace ${temporalNamespace} at ${temporalAddress}`,
    );

    await worker.run();
  } finally {
    connection.close();
  }
}

run().catch((error: unknown) => {
  console.error(error);
  process.exit(1);
});
