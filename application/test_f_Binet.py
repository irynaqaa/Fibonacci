import unittest
from fibonacci_module import f_Binet

class TestFBinetFunction(unittest.TestCase):
    def test_fibonacci_number(self):
        # Test with a Fibonacci number
        self.assertEqual(f_Binet(7), 13)
    def test_not_fibonacci_number(self):
        # Test with a not Fibonacci number
        with self.assertRaises(ValueError):
            f_Binet(6.5)
    def test_negative_number(self):
        # Test with a negative number
        with self.assertRaises(ValueError):
            f_Binet(-4)
    def test_float_input(self):
        # Test with a float input
        with self.assertRaises(TypeError):
            f_Binet(4.0)
    def test_non_numeric_input(self):
        # Test with a non-numeric input
        with self.assertRaises(TypeError):
            f_Binet("four")
    def test_edge_cases(self):
        # Test with edge case: 0
        with self.assertRaises(ValueError):
            f_Binet(0)
        # Test with edge case: 1
        self.assertEqual(f_Binet(1), 0)

if __name__ == '__main__':
    unittest.main()