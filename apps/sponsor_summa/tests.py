from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from apps.sponsor_summa.models import SponsorSumma
from apps.student.models import Student
from apps.institute.models import Institute
from apps.sponsor.models import PaymentType, Sponsor
from faker import Faker
from rest_framework import status
from django.urls import reverse


class Test(APITestCase):
    """Sponsor Summa App Tests"""

    def setUp(self) -> None:
        self._client = APIClient()

        self._faker = Faker()

        self.client = APIClient()

        self._payment_type = PaymentType.objects.create(title="Click")
        self._institute = Institute.objects.create(name="Tatu")

        self._sponsor = Sponsor.objects.create(
            full_name=self._faker.name(),
            sum=self._faker.random_int(min=100000, max=100000000, step=1000),
            phone=self._faker.random_int(
                min=100000000000, max=999999999999, step=1000),
            firm=self._faker.name(),
            spent=2000
        )
        self._student = Student.objects.create(
            full_name=self._faker.name(),
            type=Student.TYPE[0][0],
            phone=self._faker.random_int(
                min=100000000000, max=999999999999, step=1000),
            institute=self._institute,
            contract=10000000,
        )
        self._sponsor.payment_type.add(self._payment_type)
        self._sponsor_summa = SponsorSumma.objects.create(sponsor=self._sponsor, summa=10000000, student=self._student)
        self._list_url = reverse("sponsor-summa-list")

    def test_list(self):
        """Sponsor summa uchun test"""

        response = self.client.get(self._list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
