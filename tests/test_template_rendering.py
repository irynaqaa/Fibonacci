import pytest
from application.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_template_rendering(client):
    response = client.get('/fib/')
    assert response.status_code == 200
    assert b'usage.html' in response.data
