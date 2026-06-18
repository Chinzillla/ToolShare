import { Client, Connection } from '@temporalio/client';

import { temporalAddress, temporalNamespace, temporalTaskQueue } from './config.js';
import { bookingConnectionWorkflow } from './workflows.js';

async function run() {
  const connection = await Connection.connect({
    address: temporalAddress,
  });

  const client = new Client({
    connection,
    namespace: temporalNamespace,
  });

  const bookingId = `booking-${Date.now()}`;

  const handle = await client.workflow.start(bookingConnectionWorkflow, {
    args: [bookingId],
    taskQueue: temporalTaskQueue,
    workflowId: `sample-${bookingId}`,
  });

  console.log(`Started workflow ${handle.workflowId}`);

  const result = await handle.result();

  console.log(result);
}

run().catch((error: unknown) => {
  console.error(error);
  process.exit(1);
});
