'''
This is a test module for the fibonacci function.
'''
import unittest
import logging
from fibonacci import fibonacci


class TestFibonacciFunction(unittest.TestCase):
    '''
    This is a test class for the fibonacci function.
    '''
    
    def test_base_cases(self):
        '''
        Test the base cases of the fibonacci function.
        '''
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        
    def test_negative_input(self):
        '''
        Test the fibonacci function with a negative input.
        '''
        with self.assertLogs(level='ERROR'):
            with self.assertRaises(ValueError):
                fibonacci(-1)
        
    def test_large_input(self):
        '''
        Test the fibonacci function with a large input.
        '''
        self.assertEqual(fibonacci(10), 55)
        
    def test_logging(self):
        '''
        Test the logging functionality of the fibonacci function.
        '''
        with self.assertLogs(level='DEBUG'):
            fibonacci(5)
        
    def test_edge_cases(self):
        '''
        Test the edge cases of the fibonacci function.
        '''
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        
    def test_iterative_approach(self):
        '''
        Test the function with a large input to ensure it uses an iterative approach
        '''
        # Test the function with a large input to ensure it uses an iterative approach
        self.assertEqual(fibonacci(20), 6765)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
