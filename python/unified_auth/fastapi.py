from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from .jwt import verify_jwt

security = HTTPBearer()

async def require_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    jwks_url = os.getenv("JWKS_URL")
    issuer = os.getenv("JWT_ISSUER", "")
    audience = os.getenv("JWT_AUDIENCE", "")

    if jwks_url:
        try:
            user = await verify_jwt(token, jwks_url, issuer, audience)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) from e
        return user
    # If no JWKS_URL configured, simply return token for local dev
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"sub": "dev", "token": token}
