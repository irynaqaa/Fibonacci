import unittest
from fibonacci_module import fibList, phi, is_fibonacci, f_Binet, nearest_Binet_fib, make_saved_Fibonacci_file, get_nth_saved_Fibonacci_number, nearest_saved_fib
import os

class TestFibonacciModuleFunctions(unittest.TestCase):
    def test_fibList(self):
        self.assertEqual(fibList(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibList(0), [])
        self.assertEqual(fibList(1), [0])
        self.assertEqual(fibList(2), [0, 1])
        with self.assertRaises(ValueError):
            fibList(-1)

    def test_phi(self):
        self.assertAlmostEqual(phi, (1 + 5**0.5) / 2)

    def test_is_fibonacci(self):
        self.assertTrue(is_fibonacci(13))
        self.assertFalse(is_fibonacci(14))

    def test_f_Binet(self):
        self.assertEqual(f_Binet(10), 34)
        self.assertEqual(f_Binet(1), 0)
        self.assertEqual(f_Binet(2), 1)
        with self.assertRaises(ValueError):
            f_Binet(0)

    def test_nearest_Binet_fib(self):
        self.assertEqual(nearest_Binet_fib(13), 13)
        self.assertEqual(nearest_Binet_fib(14), 13)
        self.assertEqual(nearest_Binet_fib(15), 13)

    def test_make_saved_Fibonacci_file(self):
        make_saved_Fibonacci_file()
        self.assertTrue(os.path.isfile('savedFibonacciNumbers.bin'))

    def test_get_nth_saved_Fibonacci_number(self):
        self.assertEqual(get_nth_saved_Fibonacci_number(10), 34)
        self.assertEqual(get_nth_saved_Fibonacci_number(1), 0)
        self.assertEqual(get_nth_saved_Fibonacci_number(2), 1)
        with self.assertRaises(ValueError):
            get_nth_saved_Fibonacci_number(0)
        with self.assertRaises(ValueError):
            get_nth_saved_Fibonacci_number(1000000)

    def test_nearest_saved_fib(self):
        self.assertEqual(nearest_saved_fib(13), 13)
        self.assertEqual(nearest_saved_fib(14), 13)
        self.assertEqual(nearest_saved_fib(15), 13)

if __name__ == '__main__':
    unittest.main()
