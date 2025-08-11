import pytest
from app import app

@pytest.fixture
def client():
    """A test client for the app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_app_creation():
    """Test the app instance creation."""
    assert app is not None

def test_views_import():
    """Test that views module imports without errors."""
    try:
        import app.views
    except ImportError:
        pytest.fail("views module could not be imported")