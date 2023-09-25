from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class Test(APITestCase):
    """Base app tests"""

    def setUp(self) -> None:
        self._faq_url = reverse("faq")
        self._dashboard_url = reverse("dashboard")
        self._payment_type_url = reverse("payment-type")
        self.client = APIClient()

    def test_faq(self):
        """FAQ api endpoint test"""

        response = self.client.get(self._faq_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dashboard(self):
        """Dashboard api endpoint test"""

        response = self.client.get(self._dashboard_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_payment(self):
        """Payment api endpoint test"""

        response = self.client.get(self._payment_type_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
