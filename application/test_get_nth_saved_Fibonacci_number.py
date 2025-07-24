import unittest
from fibonacci_module import get_nth_saved_Fibonacci_number
import os


class TestGetNthSavedFibonacciNumberFunction(unittest.TestCase):
    
    def test_get_nth_saved_Fibonacci_number(self):
        # Test with a valid input
        make_saved_Fibonacci_file(10, "test_file.txt")
        self.assertEqual(get_nth_saved_Fibonacci_number(5, "test_file.txt"), 3)
        os.remove("test_file.txt")
        
    def test_get_nth_saved_Fibonacci_number_invalid_input(self):
        # Test with an invalid input
        make_saved_Fibonacci_file(10, "test_file.txt")
        with self.assertRaises(TypeError):
            get_nth_saved_Fibonacci_number("five", "test_file.txt")
        os.remove("test_file.txt")
        
    def test_get_nth_saved_Fibonacci_number_negative_input(self):
        # Test with a negative input
        make_saved_Fibonacci_file(10, "test_file.txt")
        with self.assertRaises(ValueError):
            get_nth_saved_Fibonacci_number(-5, "test_file.txt")
        os.remove("test_file.txt")
        
    def test_get_nth_saved_Fibonacci_number_non_numeric_input(self):
        # Test with a non-numeric input
        make_saved_Fibonacci_file(10, "test_file.txt")
        with self.assertRaises(TypeError):
            get_nth_saved_Fibonacci_number("five", "test_file.txt")
        os.remove("test_file.txt")
        
    def test_get_nth_saved_Fibonacci_number_empty_file_name(self):
        # Test with an empty file name
        with self.assertRaises(ValueError):
            get_nth_saved_Fibonacci_number(5, "")
        
    def test_get_nth_saved_Fibonacci_number_file_not_found(self):
        # Test with a file that does not exist
        with self.assertRaises(FileNotFoundError):
            get_nth_saved_Fibonacci_number(5, "non_existent_file.txt")
        
if __name__ == '__main__':
    unittest.main()