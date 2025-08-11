import pytest
import numpy as np
from noisy_input_API import add_noise

@pytest.mark.parametrize("input_data, expected_length", [
    ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 10),  # Standard case
    ([], 0),  # Edge case with empty list
    ([1], 1),  # Single Fibonacci number
    ([144, 233, 377, 610, 987], 5)  # Large Fibonacci numbers
])
def test_add_noise_length(input_data, expected_length):
    """Test add_noise function with valid inputs to check output length."""
    noisy_data = add_noise(input_data)
    assert len(noisy_data) == expected_length

@pytest.mark.parametrize("input_data", [
    ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),  # Standard case
    ([1]),  # Single Fibonacci number
    ([144, 233, 377, 610, 987])  # Large Fibonacci numbers
])
def test_add_noise_proportionality(input_data):
    """Test add_noise function to ensure noise is added proportionally."""
    noisy_data = add_noise(input_data)
    for original, noisy in zip(input_data, noisy_data):
        assert noisy != original  # Ensure noise is added
        assert noisy / original > 0.9 and noisy / original < 1.1  # Check proportionality

@pytest.mark.parametrize("input_data", [
    [],  # Edge case with empty list
    [1],  # Single Fibonacci number
])
def test_add_noise_edge_cases(input_data):
    """Test add_noise function with edge cases."""
    noisy_data = add_noise(input_data)
    assert noisy_data == [] if input_data == [] else len(noisy_data) == 1