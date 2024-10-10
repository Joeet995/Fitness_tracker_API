from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Activity

class ActivityCreateTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='TestPassword123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_activity(self):
        url = reverse('activity-list')
        data = {
            'activity_type': 'Running',
            'duration': 30,
            'distance': 5,
            'calories_burned': 300,
            'date': '2024-10-01'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.user.id)

class ActivityRetrieveTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='TestPassword123'
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='Running',
            duration=30,
            distance=5,
            calories_burned=300,
            date='2024-10-01'
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_activity(self):
        url = reverse('activity-detail', kwargs={'pk': self.activity.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['activity_type'], 'Running')


