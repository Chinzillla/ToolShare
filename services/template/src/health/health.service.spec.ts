import { HealthService } from './health.service';

describe('HealthService', () => {
    let service: HealthService;

    beforeEach(() => {
        service = new HealthService();
    });

    it('returns an ok health response', () => {
        const result = service.getHealth();

        expect(result.status).toBe('ok')
        expect(result.service).toBe('service-template')
        expect(typeof result.uptime).toBe('number')
        expect(typeof result.timestamp).toBe('string')
    })
    
})