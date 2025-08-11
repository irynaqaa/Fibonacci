import pytest
from app import app

@pytest.fixture
def client():
    """A test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("url, expected_status", [
    ('/', 200),
    ('/index', 200),
    ('/fib/5', 200),
    ('/fib/-1', 200),  # Invalid input but should render usage page
])
def test_index(client, url, expected_status):
    """Test the index and other routes."""
    response = client.get(url)
    assert response.status_code == expected_status

def test_my_fib(client):
    """Test the my_fib route with valid input."""
    response = client.get('/fib/5')
    assert b'Fibonacci' in response.data
    assert b'0' in response.data
    assert b'1' in response.data
    assert b'2' in response.data
    assert b'3' in response.data
    assert b'5' in response.data

def test_my_fib_invalid(client):
    """Test the my_fib route with invalid input."""
    response = client.get('/fib/string')
    assert b'Could not interpret' in response.data
    assert b'Please enter a positive integer' in response.data