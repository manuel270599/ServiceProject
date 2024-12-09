import unittest
from src.app import app

class TestUserManagement(unittest.TestCase):
    def test_get_users(self):
        client = app.test_client()
        response = client.get('/users')
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
