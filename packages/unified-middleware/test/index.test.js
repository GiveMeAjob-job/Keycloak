const express = require('express');
const request = require('supertest');
const middleware = require('..');

test('rejects missing token', async () => {
  const app = express();
  app.use(middleware({jwksUri: 'http://localhost/jwks', issuer: 'test', audience: 'test'}));
  app.get('/', (req, res) => res.send('ok'));
  const res = await request(app).get('/');
  expect(res.status).toBe(401);
});
