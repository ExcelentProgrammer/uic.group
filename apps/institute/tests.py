from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Institute


class Test(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self._list_url = reverse("institute:name")
        self.institute = Institute.objects.create(name="test_name")

    def test_institute_list(self):
        response = self.client.get(self._list_url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("count", data)
        self.assertIn("next", data)
        self.assertIn("results", data)
        self.assertIn("previous", data)
        self.assertEqual(len(data['results']), 1)
