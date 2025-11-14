import pytest
from application.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_fibonacci_zero(client):
    response = client.get('/fib/0')
    assert response.data == b'0'


def test_fibonacci_one(client):
    response = client.get('/fib/1')
    assert response.data == b'1'


def test_fibonacci_two(client):
    response = client.get('/fib/2')
    assert response.data == b'1, 1'


def test_fibonacci_large(client):
    response = client.get('/fib/10')
    assert response.data == b'0, 1, 1, 2, 3, 5, 8, 13, 21, 34'


def test_fibonacci_invalid(client):
    response = client.get('/fib/foo')
    assert response.status_code == 400
