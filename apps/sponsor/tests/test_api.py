from django.test import TestCase, Client
from django.urls import reverse, resolve
from apps.sponsor.models import Sponsor,PaymentType
from rest_framework.test import APIClient
from faker import Faker
from rest_framework import status

class Test(TestCase):

    def setUp(self) -> None:

        self._client = APIClient()
        
        self._faker = Faker()
        self.client = Client()


        self._payment_type = PaymentType.objects.create(title="Click")

        self._sponsor = Sponsor.objects.create(
            full_name=self._faker.name(),
            sum=self._faker.random_int(min=100000,max=100000000,step=1000),
            phone=self._faker.random_int(min=100000000000,max=999999999999,step=1000),
            firm=self._faker.name(),
            spent=2000
        )
        self._sponsor.payment_type.add(self._payment_type)


        self._detail_url = reverse("detail",kwargs={"id":self._sponsor.id})


    def test_sponsor_list(self):
        url = reverse("sponsor-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_detail(self):
        response = self._client.get(self._detail_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)