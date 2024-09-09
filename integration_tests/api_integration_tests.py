import unittest
import requests

class TestPublicAPIIntegration(unittest.TestCase):

    def test_get_post(self):
        """Test integration with a public API by fetching a post."""
        url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(url)

        # Check that the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Validate that the response is in JSON format
        self.assertEqual(response.headers["Content-Type"], "application/json; charset=utf-8")

        # Validate the content of the response
        json_response = response.json()
        self.assertEqual(json_response["id"], 1)
        self.assertIn("title", json_response)

    def test_create_post(self):
        """Test integration with a public API by creating a new post."""
        url = "https://jsonplaceholder.typicode.com/posts"
        data = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(url, json=data)

        # Check that the request was successful (status code 201 Created)
        self.assertEqual(response.status_code, 201)

        # Validate the content of the response
        json_response = response.json()
        self.assertEqual(json_response["title"], "foo")
        self.assertEqual(json_response["body"], "bar")
        self.assertEqual(json_response["userId"], 1)

if __name__ == '__main__':
    unittest.main()
