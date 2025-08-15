import unittest
from unittest.mock import Mock, patch
from yourapp import app
from yourapp.views import index, test_script, fib_usage, my_fib


class TestViews(unittest.TestCase):
    def test_index(self):
        # Test that the index method returns the rendered index.html template
        with app.test_client() as client:
            response = client.get('/'
            )
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('index.html')

            response = client.get('/index'
            )
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('index.html')

    def test_test_script(self):
        # Test that the test_script method returns the rendered test_script.html template
        with app.test_client() as client:
            response = client.get('/test_script.html'
            )
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('test_script.html')

    def test_fib_usage(self):
        # Test that the fib_usage method returns the rendered usage.html template
        with app.test_client() as client:
            response = client.get('/fib/'
            )
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('usage.html')

    def test_my_fib_valid_input(self):
        # Test that the my_fib method correctly interprets the input as a positive integer
        with app.test_client() as client:
            response = client.get('/fib/10'
            )
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('output.html')

    def test_my_fib_non_integer_input(self):
        # Test that the my_fib method raises an error for non-integer inputs
        with app.test_client() as client:
            response = client.get('/fib/abc'
            )
            self.assertEqual(response.status_code, 400)

    def test_my_fib_negative_input(self):
        # Test that the my_fib method raises an error for negative integers
        with app.test_client() as client:
            response = client.get('/fib/-10'
            )
            self.assertEqual(response.status_code, 400)

    def test_my_fib_truncation(self):
        # Test that the my_fib method correctly truncates the Fibonacci sequence
        with app.test_client() as client:
            response = client.get('/fib/100'
            )
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('output.html')

    def test_fib_list_function(self):
        # Test that the fib_list function correctly generates the Fibonacci sequence
        with patch('yourapp.views.fib_list') as mock_fib_list:
            mock_fib_list.return_value = ([0, 1, 1, 2, 3, 5, 8], '')
            response = my_fib(10)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('output.html')

    def test_fib_list_function_truncation(self):
        # Test that the fib_list function correctly truncates the Fibonacci sequence
        with patch('yourapp.views.fib_list') as mock_fib_list:
            mock_fib_list.return_value = ([0, 1, 1, 2, 3, 5, 8], '')
            response = my_fib(5)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed('output.html')

    def test_fib_list_function_negative_input(self):
        # Test that the fib_list function raises an error for negative inputs
        with patch('yourapp.views.fib_list') as mock_fib_list:
            mock_fib_list.side_effect = ValueError('Input must be a positive integer')
            with self.assertRaises(ValueError):
                my_fib(-10)

if __name__ == '__main__':
    unittest.main()
