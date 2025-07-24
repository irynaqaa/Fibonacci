import unittest
from fibonacci_module import nearest_saved_fib
import os


class TestNearestSavedFibFunction(unittest.TestCase):
    def test_nearest_saved_fib(self):
        # Test with a Fibonacci number
        make_saved_Fibonacci_file()
        self.assertEqual(nearest_saved_fib(13), 13)
        os.remove('savedFibonacciNumbers.bin')
        
    def test_nearest_saved_fib_not_fibonacci_number(self):
        # Test with a not Fibonacci number
        make_saved_Fibonacci_file()
        self.assertEqual(nearest_saved_fib(14), 13)
        os.remove('savedFibonacciNumbers.bin')
        
    def test_nearest_saved_fib_negative_number(self):
        # Test with a negative number
        make_saved_Fibonacci_file()
        with self.assertRaises(ValueError):
            nearest_saved_fib(-4)
        os.remove('savedFibonacciNumbers.bin')
        
    def test_nearest_saved_fib_float_input(self):
        # Test with a float input
        make_saved_Fibonacci_file()
        self.assertEqual(nearest_saved_fib(13.0), 13)
        os.remove('savedFibonacciNumbers.bin')
        
    def test_nearest_saved_fib_non_numeric_input(self):
        # Test with a non-numeric input
        make_saved_Fibonacci_file()
        with self.assertRaises(TypeError):
            nearest_saved_fib("four")
        os.remove('savedFibonacciNumbers.bin')
        
    def test_nearest_saved_fib_edge_cases(self):
        # Test with edge case: 0
        make_saved_Fibonacci_file()
        self.assertEqual(nearest_saved_fib(0), 0)
        os.remove('savedFibonacciNumbers.bin')
        # Test with edge case: 1
        make_saved_Fibonacci_file()
        self.assertEqual(nearest_saved_fib(1), 1)
        os.remove('savedFibonacciNumbers.bin')
        
if __name__ == '__main__':
    unittest.main()