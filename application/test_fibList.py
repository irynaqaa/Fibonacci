import unittest
from fibonacci_module import fibList


class TestFibListFunction(unittest.TestCase):
    
    def test_fibList(self):
        # Test with a positive integer
        self.assertEqual(fibList(5), [0, 1, 1, 2, 3])
        
    def test_fibList_invalid_input(self):
        # Test with an invalid input
        with self.assertRaises(TypeError):
            fibList(5.5)
        
    def test_fibList_negative_input(self):
        # Test with a negative input
        with self.assertRaises(ValueError):
            fibList(-5)
        
    def test_fibList_non_numeric_input(self):
        # Test with a non-numeric input
        with self.assertRaises(TypeError):
            fibList("five")
        
    def test_fibList_zero(self):
        # Test with zero
        self.assertEqual(fibList(0), [])
        
    def test_fibList_one(self):
        # Test with one
        self.assertEqual(fibList(1), [0])
        
if __name__ == '__main__':
    unittest.main()
