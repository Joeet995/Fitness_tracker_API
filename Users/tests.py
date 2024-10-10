from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        url = reverse('user-create')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'TestPassword123',
            'first_name': 'John',
            'last_name': 'Doe',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'testuser')



