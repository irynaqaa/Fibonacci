import unittest
from fibonacci import FIRSTPOINTS, PREDICTPOINT
from fibonacci_module import fibList, phi, is_fibonacci, f_Binet, nearest_Binet_fib, make_saved_Fibonacci_file, get_nth_saved_Fibonacci_number, nearest_saved_fib, nearest_saved_fib_index
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error


class TestFibonacci(unittest.TestCase):
    def test_fibList(self):
        # Test that the fibList function correctly generates the Fibonacci sequence
        num = 10
        fib_numbers = fibList(num)
        self.assertEqual(len(fib_numbers), num)

    def test_phi(self):
        # Test that the phi constant is correctly defined
        self.assertAlmostEqual(phi, (1 + 5**0.5) / 2)

    def test_is_fibonacci(self):
        # Test that the is_fibonacci function correctly identifies Fibonacci numbers
        fib_number = 13
        self.assertTrue(is_fibonacci(fib_number))

    def test_f_Binet(self):
        # Test that the f_Binet function correctly calculates the nth Fibonacci number
        n = 7
        fib_number = f_Binet(n)
        self.assertEqual(fib_number, 13)

    def test_nearest_Binet_fib(self):
        # Test that the nearest_Binet_fib function correctly finds the nearest Fibonacci number to a given number
        num = 15
        nearest_fib = nearest_Binet_fib(num)
        self.assertEqual(nearest_fib, 13)

    def test_make_saved_Fibonacci_file(self):
        # Test that the make_saved_Fibonacci_file function correctly creates a file containing the first MAX_NUMBER_OF_SAVED_DIGITS Fibonacci numbers
        make_saved_Fibonacci_file()
        self.assertTrue(os.path.isfile('savedFibonacciNumbers.bin'))

    def test_get_nth_saved_Fibonacci_number(self):
        # Test that the get_nth_saved_Fibonacci_number function correctly retrieves the nth Fibonacci number from the saved file
        n = 7
        fib_number = get_nth_saved_Fibonacci_number(n)
        self.assertEqual(fib_number, 13)

    def test_nearest_saved_fib(self):
        # Test that the nearest_saved_fib function correctly finds the nearest Fibonacci number to a given number using the saved file
        num = 15
        nearest_fib = nearest_saved_fib(num)
        self.assertEqual(nearest_fib, 13)

    def test_nearest_saved_fib_index(self):
        # Test that the nearest_saved_fib_index function correctly finds the index of the nearest Fibonacci number to a given number using the saved file
        num = 15
        index = nearest_saved_fib_index(num)
        self.assertEqual(index, 7)

    def test_fit(self):
        # Test that the fit function correctly fits a line to the log of the Fibonacci numbers
        x = list(range(1, FIRSTPOINTS + 1))
        y = fibList(FIRSTPOINTS)
        log_x = x[1:]
        log_y = [math.log(fibNum) for fibNum in y[1:]]
        popt, pcov = curve_fit(lambda x, m, b: m * x + b, log_x, log_y)
        self.assertAlmostEqual(popt[0], math.log(phi), places=2)

    def test_predict(self):
        # Test that the predict function correctly predicts the nth Fibonacci number using the fit
        n = PREDICTPOINT
        predicted_fib = math.exp(curve_fit(lambda x, m, b: m * x + b, list(range(1, FIRSTPOINTS + 1)), [math.log(fib) for fib in fibList(FIRSTPOINTS)])[0][0] * n + curve_fit(lambda x, m, b: m * x + b, list(range(1, FIRSTPOINTS + 1)), [math.log(fib) for fib in fibList(FIRSTPOINTS)])[0][1])
        self.assertAlmostEqual(predicted_fib, fibList(PREDICTPOINT)[-1], places=2)

if __name__ == '__main__':
    unittest.main()
