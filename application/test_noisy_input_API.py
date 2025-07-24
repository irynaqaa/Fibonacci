import unittest
from application.Fibonacci.noisy_input_API import add_noise, get_data
import numpy as np


class TestNoisyInputAPI(unittest.TestCase):
    def test_add_noise(self):
        # Test the function with different inputs
        test_cases = [
            ([1, 2, 3], [1.1, 2.2, 3.3]),
            ([4, 5, 6], [4.4, 5.5, 6.6]),
        ]
        for input_value, expected_output in test_cases:
            self.assertTrue(np.allclose(add_noise(input_value), expected_output, atol=0.2))
        
    def test_get_data(self):
        # Test the function with different inputs
        test_cases = [
            (1, [1]),
            (2, [1, 2]),
        ]
        for input_value, expected_output in test_cases:
            self.assertEqual(len(get_data(input_value)), len(expected_output))
        
    def test_get_data_edge_cases(self):
        # Test the function with edge cases
        test_cases = [
            (0, []),
            (-1, []),
        ]
        for input_value, expected_output in test_cases:
            self.assertEqual(get_data(input_value), expected_output)
        
    def test_get_data_invalid_input(self):
        # Test the function with invalid input
        test_cases = [
            ('a', []),
            (None, []),
        ]
        for input_value, expected_output in test_cases:
            with self.assertRaises(TypeError):
                get_data(input_value)
        
if __name__ == '__main__':
    unittest.main()
