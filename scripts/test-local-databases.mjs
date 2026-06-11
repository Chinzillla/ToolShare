import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import test from 'node:test';

const services = [
  {
    name: 'user',
    database: 'toolshare_user_db',
    role: 'toolshare_user_service',
    password: 'toolshare-user-local',
  },
  {
    name: 'catalog',
    database: 'toolshare_catalog_db',
    role: 'toolshare_catalog_service',
    password: 'toolshare-catalog-local',
  },
  {
    name: 'booking',
    database: 'toolshare_booking_db',
    role: 'toolshare_booking_service',
    password: 'toolshare-booking-local',
  },
  {
    name: 'payment',
    database: 'toolshare_payment_db',
    role: 'toolshare_payment_service',
    password: 'toolshare-payment-local',
  },
  {
    name: 'review',
    database: 'toolshare_review_db',
    role: 'toolshare_review_service',
    password: 'toolshare-review-local',
  },
  {
    name: 'notification',
    database: 'toolshare_notification_db',
    role: 'toolshare_notification_service',
    password: 'toolshare-notification-local',
  },
  {
    name: 'admin',
    database: 'toolshare_admin_db',
    role: 'toolshare_admin_service',
    password: 'toolshare-admin-local',
  },
  {
    name: 'risk',
    database: 'toolshare_risk_db',
    role: 'toolshare_risk_service',
    password: 'toolshare-risk-local',
  },
];

function runPsql({ database, role = 'toolshare', password = 'toolshare' }, sql) {
  return spawnSync(
    'docker',
    [
      'exec',
      '-e',
      `PGPASSWORD=${password}`,
      'toolshare-postgres',
      'psql',
      '-h',
      'localhost',
      '-U',
      role,
      '-d',
      database,
      '-tAc',
      sql,
    ],
    {
      encoding: 'utf8',
      shell: false,
    },
  );
}

test('each service can connect to its own database', () => {
  for (const service of services) {
    const result = runPsql(
      {
        database: service.database,
        role: service.role,
        password: service.password,
      },
      'SELECT current_database();',
    );

    assert.equal(
      result.status,
      0,
      `${service.name} connection failed: ${result.stderr}`,
    );

    assert.equal(result.stdout.trim(), service.database);
  }
});

test('each service cannot connect to another service database with a wrong user', () => {
    for (const [index, service] of services.entries()) {
        const otherService = services[(index + 1) % services.length];

        const result = runPsql(
            {
                database: otherService.database,
                role: service.role,
                password: service.password,
            },
            'SELECT current_database();',
        );
        
        assert.notEqual(
            result.status,
            0,
            `${service.name} unexpectedly connected to ${otherService.database}`,
        );

        assert.match(
            result.stderr,
            /permission denied for database/,
            `Expected a permission error but received: ${result.stderr}`,
        );
    }
})
