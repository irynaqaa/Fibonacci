import unittest
from unittest.mock import Mock, patch
from noisy_input_API import add_noise, get_data
import numpy as np


class TestNoisyInputAPI(unittest.TestCase):
    def test_add_noise(self):
        # Test that the add_noise function correctly adds Gaussian noise to a list of pure data
        pure_data = [1, 2, 3, 4, 5]
        noisy_data = add_noise(pure_data)
        self.assertEqual(len(noisy_data), len(pure_data))

    def test_add_noise_empty_list(self):
        # Test that the add_noise function handles an empty input list
        pure_data = []
        noisy_data = add_noise(pure_data)
        self.assertEqual(len(noisy_data), len(pure_data))

    def test_get_data(self):
        # Test that the get_data function correctly generates a specified number of random Fibonacci numbers with added Gaussian noise
        how_much = 10
        data = get_data(how_much)
        self.assertEqual(len(data), how_much)

    def test_get_data_non_positive_input(self):
        # Test that the get_data function raises an error for non-positive input
        how_much = -1
        with self.assertRaises(ValueError):
            get_data(how_much)

    def test_get_data_invalid_fibonacci_number_range(self):
        # Test that the get_data function raises an error for invalid Fibonacci number range
        how_much = 1001
        with self.assertRaises(ValueError):
            get_data(how_much)

    def test_integration_with_fibList(self):
        # Test that the get_data function correctly integrates with the fibList function from the fibonacci_module
        how_much = 10
        data = get_data(how_much)
        self.assertEqual(len(data), how_much)

if __name__ == '__main__':
    unittest.main()
