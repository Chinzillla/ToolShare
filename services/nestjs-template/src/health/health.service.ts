import { Injectable } from '@nestjs/common';

@Injectable()
export class HealthService {
    getHealth() {
        return {
            status: 'ok',
            service: 'service-template',
            uptime: process.uptime(),
            timestamp: new Date().toISOString(),
        };
    }
}