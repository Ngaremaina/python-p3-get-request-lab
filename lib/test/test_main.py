import pytest
from ..main import app
from fastapi.testclient import TestClient

@pytest.fixture(scope='session')
def client():
    return TestClient(app)

def test_root(client: TestClient):
    res = client.get('/')
    assert res.status_code == 200, "unsuccesful request"
    assert res.json() == {"message" : "Welcome to Kenya"} , "Unexpected json response"
