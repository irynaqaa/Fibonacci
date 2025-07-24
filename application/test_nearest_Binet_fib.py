import unittest
from fibonacci_module import nearest_Binet_fib


class TestNearestBinetFibFunction(unittest.TestCase):
    
    def test_fibonacci_number(self):
        # Test with a Fibonacci number
        self.assertEqual(nearest_Binet_fib(13), 13)
        
    def test_not_fibonacci_number(self):
        # Test with not a Fibonacci number
        self.assertEqual(nearest_Binet_fib(14), 13)
        
    def test_negative_number(self):
        # Test with a negative number
        with self.assertRaises(ValueError):
            nearest_Binet_fib(-4)
        
    def test_float_input(self):
        # Test with a float input
        self.assertEqual(nearest_Binet_fib(13.0), 13)
        
    def test_non_numeric_input(self):
        # Test with a non-numeric input
        with self.assertRaises(TypeError):
            nearest_Binet_fib("four")
        
    def test_edge_cases(self):
        # Test with edge case: 0
        self.assertEqual(nearest_Binet_fib(0), 0)
        # Test with edge case: 1
        self.assertEqual(nearest_Binet_fib(1), 1)
        
if __name__ == '__main__':
    unittest.main()
