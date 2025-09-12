from django.test import TestCase
from rest_framework.test import APIClient

class HelloWorldTest(TestCase):
    def test_hello_world(self):
        client = APIClient()
        response = client.get('/api/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Hello, World!"})