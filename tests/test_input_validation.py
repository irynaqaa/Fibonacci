import pytest
from application.fibonacci import validate_input


def test_validate_input_valid():
    """Test input validation with valid inputs."""
    assert validate_input("10") == 10
    assert validate_input("0") == 0


def test_validate_input_invalid():
    """Test input validation with invalid inputs."""
    with pytest.raises(ValueError):
        validate_input("-5")
    with pytest.raises(ValueError):
        validate_input("abc")
    with pytest.raises(ValueError):
        validate_input(5.5)
