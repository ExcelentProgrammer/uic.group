from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse


# Create your tests here.
class Test(APITestCase):

    def setUp(self) -> None:
        self._list_url = reverse("student:list")
        self.client = APIClient()

    def test_list(self):
        """Student list endpoint test"""

        response = self.client.get(self._list_url)
        self.assertEqual(response.status_code, 200)
