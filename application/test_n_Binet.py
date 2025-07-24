import unittest
from fibonacci_module import n_Binet


class TestNBinetFunction(unittest.TestCase):
    
    def test_fibonacci_number(self):
        # Test with a Fibonacci number
        self.assertEqual(n_Binet(13), 7)
        
    def test_not_fibonacci_number(self):
        # Test with not a Fibonacci number
        self.assertAlmostEqual(n_Binet(14), 7.0, delta=1)
        
    def test_negative_number(self):
        # Test with a negative number
        with self.assertRaises(ValueError):
            n_Binet(-4)
        
    def test_float_input(self):
        # Test with a float input
        self.assertAlmostEqual(n_Binet(13.0), 7.0, delta=1)
        
    def test_non_numeric_input(self):
        # Test with a non-numeric input
        with self.assertRaises(TypeError):
            n_Binet("four")
        
    def test_edge_cases(self):
        # Test with edge case: 0
        self.assertEqual(n_Binet(0), 0)
        # Test with edge case: 1
        self.assertEqual(n_Binet(1), 1)
        
if __name__ == '__main__':
    unittest.main()
