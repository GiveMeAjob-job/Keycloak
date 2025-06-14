import sys
import pytest

sys.path.insert(0, 'python')
from unified_auth import verify_jwt


import asyncio


def test_invalid_token():
    with pytest.raises(Exception):
        asyncio.run(verify_jwt('bad', 'http://localhost/jwks', 'test', 'test'))
