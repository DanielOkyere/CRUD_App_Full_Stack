from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "API is Alive"}