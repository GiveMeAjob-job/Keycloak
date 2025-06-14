import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 500 },
    { duration: '5m', target: 500 }
  ],
  thresholds: {
    http_req_duration: ['p(95)<250'],
    checks: ['rate>0.999']
  }
};

export default function () {
  const url = 'https://auth.example.com/realms/master/protocol/openid-connect/token';
  const payload = 'grant_type=password&client_id=cli&username=test&password=test';
  const params = { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } };
  const res = http.post(url, payload, params);
  check(res, { 'status 200': r => r.status === 200 });
  sleep(1);
}
