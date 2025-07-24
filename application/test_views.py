import unittest
from unittest.mock import patch, MagicMock
from views import app
import json


class TestViewsPy(unittest.TestCase):
    @patch('views.render_template')
    def test_index(self, mock_render_template):
        # Arrange
        mock_render_template.return_value = 'Index Page'
        
        # Act
        from views import index
        result = index()
        
        # Assert
        self.assertEqual(result, 'Index Page')
        mock_render_template.assert_called_once_with('index.html', title="Home")

    @patch('views.render_template')
    def test_test_script(self, mock_render_template):
        # Arrange
        mock_render_template.return_value = 'Test Script Page'
        
        # Act
        from views import test_script
        result = test_script()
        
        # Assert
        self.assertEqual(result, 'Test Script Page')
        mock_render_template.assert_called_once_with('test_script.html')

    @patch('views.render_template')
    def test_fib_usage(self, mock_render_template):
        # Arrange
        mock_render_template.return_value = 'Fib Usage Page'
        
        # Act
        from views import fib_usage
        result = fib_usage()
        
        # Assert
        self.assertEqual(result, 'Fib Usage Page')
        mock_render_template.assert_called_once_with('usage.html')

    @patch('views.render_template')
    def test_myFib(self, mock_render_template):
        # Arrange
        mock_render_template.return_value = 'My Fib Page'
        
        # Act
        from views import myFib
        result = myFib('10')
        
        # Assert
        self.assertEqual(result, 'My Fib Page')
        mock_render_template.assert_called_once_with('output.html', num=10, list=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34], msg='')

if __name__ == '__main__':
    unittest.main()
