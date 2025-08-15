import unittest
from unittest.mock import Mock, patch
from yourapp import app


class TestInitFunctions(unittest.TestCase):
    def test_app(self):
        self.assertIsNotNone(app)
        
    def test_app_config(self):
        # Test that the app instance has the expected configuration settings
        self.assertIn('SECRET_KEY', app.config)
        self.assertIn('DEBUG', app.config)
        self.assertIn('SQLALCHEMY_DATABASE_URI', app.config)
    
    def test_views_module(self):
        # Test that the views module is properly imported from the app package
        from yourapp import views
        self.assertIsNotNone(views)
    
    def test_app_registration(self):
        # Test that the views module is correctly registered with the app instance
        self.assertIn('views', app.blueprints)


if __name__ == '__main__':
    unittest.main()
