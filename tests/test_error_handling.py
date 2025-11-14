from application.app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_invalid_fibonacci_input(client):
    """
    Test error handling for invalid Fibonacci input.
    """
    response = client.get('/fib/-1')
    assert response.status_code == 400
    assert b'Error' in response.data


def test_invalid_fibonacci_api(client):
    """
    Test error handling for invalid Fibonacci API input.
    """
    response = client.get('/fib/abc')
    assert response.status_code == 400
    assert b'Error' in response.data
