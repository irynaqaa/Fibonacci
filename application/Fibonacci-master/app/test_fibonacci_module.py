import pytest
from fibonacci_module import fibList

@pytest.mark.parametrize("input_value, expected_output", [
    (0, []),
    (1, [0]),
    (2, [0, 1]),
    (5, [0, 1, 1, 2, 3]),
    (15, [0, 1, 1, 2, 3, 5, 8, 13]),
    (100, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]),
])
def test_fibList_valid_inputs(input_value, expected_output):
    """Test fibList with valid integer inputs."""
    assert fibList(input_value) == expected_output

@pytest.mark.parametrize("input_value", [
    (-1,),
    (-5,),
    ("string",),
    (3.2,),
    (4.9,),
])
def test_fibList_invalid_inputs(input_value):
    """Test fibList with invalid inputs that should raise exceptions."""
    with pytest.raises(ValueError):
        fibList(input_value)
