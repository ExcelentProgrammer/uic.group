from django.test import SimpleTestCase, Client
from django.urls import resolve,reverse
from apps.sponsor.views import SponsorListApi


class Test(SimpleTestCase):

    def setUp(self) -> None:
        pass

    def test_urls(self):
        url = reverse("sponsor-list")
        self.assertEqual(resolve(url).func.view_class, SponsorListApi)
