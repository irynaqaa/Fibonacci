import unittest
from app import app, db, Pet

class PetsEndpointTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_pets.db'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_pets_valid(self):
        response = self.app.get('/pets?page=1&limit=10')
        self.assertEqual(response.status_code, 200)

    def test_get_pets_invalid_page(self):
        response = self.app.get('/pets?page=-1&limit=10')
        self.assertEqual(response.status_code, 400)

    def test_get_pets_invalid_limit(self):
        response = self.app.get('/pets?page=1&limit=200')
        self.assertEqual(response.status_code, 400)

    def test_get_pets_no_pets(self):
        response = self.app.get('/pets?page=1&limit=10')
        self.assertEqual(response.json['pets'], [])

if __name__ == '__main__':
    unittest.main()
