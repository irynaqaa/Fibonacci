
import unittest
from fibonacci_module import make_saved_Fibonacci_file
import os


class TestMakeSavedFibonacciFileFunction(unittest.TestCase):
    
    def test_make_saved_Fibonacci_file(self):
        # Test with a valid input
        make_saved_Fibonacci_file(10, "test_file.txt")
        self.assertTrue(os.path.exists("test_file.txt"))
        os.remove("test_file.txt")
        
    def test_make_saved_Fibonacci_file_invalid_input(self):
        # Test with an invalid input
        with self.assertRaises(TypeError):
            make_saved_Fibonacci_file("ten", "test_file.txt")
        
    def test_make_saved_Fibonacci_file_negative_input(self):
        # Test with a negative input
        with self.assertRaises(ValueError):
            make_saved_Fibonacci_file(-10, "test_file.txt")
        
    def test_make_saved_Fibonacci_file_non_numeric_input(self):
        # Test with a non-numeric input
        with self.assertRaises(TypeError):
            make_saved_Fibonacci_file("ten", "test_file.txt")
        
    def test_make_saved_Fibonacci_file_empty_file_name(self):
        # Test with an empty file name
        with self.assertRaises(ValueError):
            make_saved_Fibonacci_file(10, "")
        
if __name__ == '__main__':
    unittest.main()
