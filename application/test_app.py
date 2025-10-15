import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_register_email_password(client):
    response = client.post('/api/register', json={'email': 'test@example.com', 'password': 'Password123!'} )
    assert response.status_code == 201
    assert b'test@example.com' in response.data


def test_register_google_oauth(client):
    response = client.post('/api/register', json={'googleToken': 'dummy_google_token'})
    assert response.status_code == 201


def test_register_invalid_password(client):
    response = client.post('/api/register', json={'email': 'test@example.com', 'password': 'short'})
    assert response.status_code == 400
    assert b'Password must be at least 8 characters long' in response.data
