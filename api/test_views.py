from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class HelloWorldTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='testpassword', id=1)

    def test_hello_world(self):
        client = APIClient()
        response = client.get('/api/hello/?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('user', response.data)