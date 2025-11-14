import pytest
from application.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Start Page' in response.data


def test_fib_usage(client):
    response = client.get('/fib/')
    assert response.status_code == 200
    assert b'Usage of Fibonacci Calculator' in response.data
