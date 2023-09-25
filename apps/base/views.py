from django.db.models import Count
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.base.models import Faq, PaymentType
from apps.base.serializers import FaqSerializer, PaymentTypeSerializer
from apps.sponsor.models import Sponsor
from apps.student.models import Student


class FaqListApi(ListAPIView):
    model = Faq
    serializer_class = FaqSerializer
    queryset = Faq.objects.order_by("id")


class DashboardApi(APIView):

    def get(self, request):
        res = Sponsor.objects.annotate(created_at=Count("created_at"))
        print(res)

        sponsors = self.get_monthly_data(Sponsor)
        students = self.get_monthly_data(Student)

        return Response({
            "sponsors": sponsors,
            "students": students
        })

    def get_monthly_data(self, model):
        """Yillik statistikani olish uchun funcsiya"""

        monthly_data = []

        for month in range(1, 13):
            records = model.objects.filter(created_at__month=month)
            if records.count() > 0:
                name = records.first().created_at.strftime("%B")
                monthly_data.append({
                    "Label": name,
                    "value": records.count()
                })
        return monthly_data


class PaymentTypeApi(ListAPIView):
    """To'lov turlarini ro'yhatini olish uchun List View"""

    model = PaymentType
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.order_by("id")
