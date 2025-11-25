import pytest
from application.fibonacci import fibList

TRUNCATE_AFTER_THIS_MANY = 10000


def test_fibList_valid_input():
    """Test Fibonacci generation with valid input."""
    assert fibList(0) == [0]
    assert fibList(1) == [0, 1]
    assert fibList(2) == [0, 1, 1]
    assert fibList(3) == [0, 1, 1, 2]
    assert fibList(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibList_truncation():
    """Test Fibonacci generation with truncation."""
    fib_numbers, message = fibList(20000)
    assert len(fib_numbers) == TRUNCATE_AFTER_THIS_MANY
    assert "Output truncated" in message


def test_fibList_invalid_input():
    """Test Fibonacci generation with invalid input."""
    with pytest.raises(ValueError):
        fibList(-1)
    with pytest.raises(ValueError):
        fibList("invalid")
