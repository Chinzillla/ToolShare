import { spawnSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const repositoryRoot = resolve(scriptDirectory, '..');
const composeFile = resolve(repositoryRoot, 'infra', 'docker-compose.yml');
const postgresVolume = 'toolshare-infra_postgres-data';
const confirmed = process.argv.includes('--yes');

if (!confirmed) {
  console.error('This command deletes all local PostgreSQL data.');
  console.error('Run again with: pnpm db:reset --yes');
  process.exit(1);
}

function run(command, args) {
  console.log(`> ${command} ${args.join(' ')}`);

  const result = spawnSync(command, args, {
    cwd: repositoryRoot,
    stdio: 'inherit',
    shell: false,
  });

  if (result.error) {
    throw result.error;
  }

  if (result.status !== 0) {
    throw new Error(`Command failed with exit code ${result.status}`);
  }
}

console.log('Resetting all local ToolShare service databases.');
console.log('Warning: all local PostgreSQL data will be deleted.');

run('docker', ['compose', '-f', composeFile, 'rm', '-sf', 'postgres']);

const volumeExists = spawnSync(
  'docker',
  ['volume', 'inspect', postgresVolume],
  {
    cwd: repositoryRoot,
    stdio: 'ignore',
    shell: false,
  },
);

if (volumeExists.status === 0) {
  run('docker', ['volume', 'rm', postgresVolume]);
}

run('docker', [
  'compose',
  '-f',
  composeFile,
  'up',
  '-d',
  '--wait',
  'postgres',
]);

console.log('Local service databases were reset successfully.');