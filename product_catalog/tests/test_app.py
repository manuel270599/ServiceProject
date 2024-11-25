import unittest
from src.app import app

class TestProductCatalog(unittest.TestCase):
    def test_get_products(self):
        client = app.test_client()
        response = client.get('/products')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
