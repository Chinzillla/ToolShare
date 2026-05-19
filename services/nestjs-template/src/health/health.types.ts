export type HealthResponse = {
  status: 'ok';
  service: string;
  uptime: number;
  timestamp: string;
};
