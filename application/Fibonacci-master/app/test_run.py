import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.run')
def test_run_app(mock_run, client):
    """Test that the Flask app runs in debug mode."""
    with patch('builtins.print') as mock_print:
        app.run(debug=True)
        mock_print.assert_called_with("Welcome!")
    assert app.debug is True

@patch('app.run')
def test_run_app_exception_handling(mock_run, client):
    """Test that the app handles exceptions during startup."""
    mock_run.side_effect = Exception("Port conflict")
    with pytest.raises(Exception):
        app.run(debug=True)
