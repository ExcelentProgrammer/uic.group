from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from apps.accounts.models import User


class Test(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self._login_path = reverse("token_obtain_pair")
        self._refresh_path = reverse("token_refresh")

        self.user = User.objects.create_user(username="test_user", password="test_password")

    def test_jwt(self):
        payload = {
            "username": "test_user",
            'password': "test_password"
        }
        response = self.client.post(self._login_path, data=payload)
        data = response.json()
        self._refresh = data.get("refresh")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", data)
        self.assertIn("refresh", data)

        payload = {
            "refresh": self._refresh
        }
        response = self.client.post(self._refresh_path, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.json())
