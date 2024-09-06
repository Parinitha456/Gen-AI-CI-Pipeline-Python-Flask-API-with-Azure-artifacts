# integration_tests/test_integration.py

import unittest
import requests

class TestIntegration(unittest.TestCase):
    def test_endpoint(self):
        response = requests.get('http://localhost:5000/api/endpoint')
        self.assertEqual(response.status_code, 200)
        self.assertIn('expected_key', response.json())

if __name__ == '__main__':
    unittest.main()
