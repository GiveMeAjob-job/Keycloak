import pytest
import sys
sys.path.insert(0, 'python')
from unified_auth import verify_jwt

@pytest.mark.asyncio
async def test_invalid_token():
    with pytest.raises(Exception):
        await verify_jwt('bad', 'http://localhost/jwks', 'test', 'test')
