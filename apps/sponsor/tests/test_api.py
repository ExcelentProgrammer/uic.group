from django.test import TestCase, Client
from django.urls import reverse, resolve


class Test(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_sponsor_list(self):
        url = reverse("sponsor-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
