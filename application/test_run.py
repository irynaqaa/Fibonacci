import unittest
from unittest.mock import patch
from run import app
import json


class TestRunPy(unittest.TestCase):
    @patch('flask.Flask')
    def test_app_creation(self, mock_flask):
        # Arrange
        mock_flask.return_value = mock_flask
        
        # Act
        from run import app
        
        # Assert
        self.assertEqual(app, mock_flask)
        mock_flask.assert_called_once_with(__name__)

    @patch('run.app')
    def test_run_app(self, mock_app):
        # Arrange
        mock_app.run.return_value = None
        
        # Act
        from run import app
        app.run(debug=True)
        
        # Assert
        mock_app.run.assert_called_once_with(debug=True)


if __name__ == '__main__':
    unittest.main()
