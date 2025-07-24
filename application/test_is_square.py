import unittest
from fibonacci_module import is_square


class TestIsSquareFunction(unittest.TestCase):
    
    def test_perfect_square(self):
        # Test with perfect square
        self.assertTrue(is_square(16))
        
    def test_not_perfect_square(self):
        # Test with not perfect square
        self.assertFalse(is_square(20))
        
    def test_negative_number(self):
        # Test with negative number
        self.assertFalse(is_square(-4))
        
    def test_float_input(self):
        # Test with float input
        self.assertTrue(is_square(4.0))
        
    def test_non_numeric_input(self):
        # Test with non-numeric input
        with self.assertRaises(TypeError):
            is_square("four")
        
    def test_edge_cases(self):
        # Test with edge case: 0
        self.assertTrue(is_square(0))
        # Test with edge case: 1
        self.assertTrue(is_square(1))
        
if __name__ == '__main__':
    unittest.main()
