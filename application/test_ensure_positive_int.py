import unittest
from fibonacci_module import ensure_positive_int


class TestEnsurePositiveIntFunction(unittest.TestCase):
    
    def test_ensure_positive_int(self):
        # Test with a positive integer
        self.assertEqual(ensure_positive_int(5), 5)
        
    def test_ensure_positive_int_invalid_input(self):
        # Test with an invalid input
        with self.assertRaises(TypeError):
            ensure_positive_int(5.5)
        
    def test_ensure_positive_int_negative_input(self):
        # Test with a negative input
        with self.assertRaises(ValueError):
            ensure_positive_int(-5)
        
    def test_ensure_positive_int_non_numeric_input(self):
        # Test with a non-numeric input
        with self.assertRaises(TypeError):
            ensure_positive_int("five")
        
    def test_ensure_positive_int_zero(self):
        # Test with zero
        with self.assertRaises(ValueError):
            ensure_positive_int(0)
        
if __name__ == '__main__':
    unittest.main()
