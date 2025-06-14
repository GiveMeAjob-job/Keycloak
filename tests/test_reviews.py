import sys
sys.path.insert(0, 'bear_review_api')
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_and_list_review():
    headers = {"Authorization": "Bearer testtoken"}
    resp = client.post('/reviews/', json={'user_id': 1, 'content': 'hello'}, headers=headers)
    assert resp.status_code == 201
    data = resp.json()
    assert data['id'] == 1

    resp = client.get('/reviews/', headers=headers)
    assert resp.status_code == 200
    items = resp.json()
    assert len(items) == 1
