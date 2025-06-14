const fetch = require('node:https').request;
const jwksCache = {};
async function getKey(jwksUri, kid) {
  if (!jwksCache[jwksUri]) {
    const data = await new Promise((resolve, reject) => {
      const req = require('https').get(jwksUri, res => {
        let body = '';
        res.on('data', c => body += c);
        res.on('end', () => resolve(JSON.parse(body)));
      });
      req.on('error', reject);
    });
    jwksCache[jwksUri] = data.keys.reduce((m, k) => (m[k.kid] = k, m), {});
  }
  return jwksCache[jwksUri][kid];
}

module.exports = function(opts) {
  const jwksUri = opts.jwksUri;
  return async function(req, res, next) {
    const auth = req.headers['authorization'];
    if (!auth) return res.status(401).end();
    const token = auth.split(' ')[1];
    const jose = await import('jose');
    const { payload } = await jose.jwtVerify(token, async (header) => {
      const key = await getKey(jwksUri, header.kid);
      return jose.importJWK(key);
    }, { algorithms: ['RS256'], issuer: opts.issuer, audience: opts.audience });
    req.user = payload;
    next();
  };
};
