import httpx
from jose import jwt
from functools import lru_cache

@lru_cache(maxsize=1)
async def get_jwks(url: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()

async def verify_jwt(token: str, jwks_url: str, issuer: str, audience: str):
    jwks = await get_jwks(jwks_url)
    key = jwks['keys'][0]
    return jwt.decode(token, key, algorithms=['RS256'], issuer=issuer, audience=audience)
