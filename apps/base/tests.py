from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


# Create your tests here.
class Test(APITestCase):

    def setUp(self) -> None:
        self._faq_url = reverse("faq")
        self._dashboard_url = reverse("dashboard")
        self._payment_type_url = reverse("payment-type")
        self.client = APIClient()

    def test_faq(self):
        response = self.client.get(self._faq_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dashboard(self):
        response = self.client.get(self._dashboard_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_payment(self):
        response = self.client.get(self._payment_type_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
