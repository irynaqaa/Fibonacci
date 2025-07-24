import unittest
from fibonacci_module import is_fibonacci

class TestIsFibonacciFunction(unittest.TestCase):
    def test_fibonacci_number(self):
        # Test with a Fibonacci number
        self.assertTrue(is_fibonacci(13))
    
    def test_not_fibonacci_number(self):
        # Test with not a Fibonacci number
        self.assertFalse(is_fibonacci(14))
    
    def test_negative_number(self):
        # Test with a negative number
        self.assertFalse(is_fibonacci(-4))
    
    def test_float_input(self):
        # Test with a float input
        with self.assertRaises(TypeError):
            is_fibonacci(4.0)
    
    def test_non_numeric_input(self):
        # Test with a non-numeric input
        with self.assertRaises(TypeError):
            is_fibonacci("four")
    
    def test_edge_cases(self):
        # Test with edge case: 0
        self.assertTrue(is_fibonacci(0))
        # Test with edge case: 1
        self.assertTrue(is_fibonacci(1))

if __name__ == '__main__':
    unittest.main()