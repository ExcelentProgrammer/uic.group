from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.base.models import Faq, PaymentType
from apps.base.serializers import FaqSerializer, PaymentTypeSerializer
from apps.sponsor.models import Sponsor
from apps.student.models import Student
from django.utils.translation import gettext as _
from django.utils import translation

class FaqListApi(ListAPIView):
    model = Faq
    serializer_class = FaqSerializer
    queryset = Faq.objects.all()


class DashboardApi(APIView):

    def get(self, request):
        sponsors = []
        students = []

        for m in range(1, 13):
            month = Sponsor.objects.filter(created_at__month=m)
            if month.count() == 0:
                continue

            name = month.first().created_at.strftime("%B")
            sponsors.append({
                "Label": name,
                "value": month.count()
            })

        for m in range(1, 13):
            month = Student.objects.filter(created_at__month=m)
            if month.count() == 0:
                continue

            name = month.first().created_at.strftime("%B")
            students.append({
                "Label": name,
                "value": month.count()
            })
        return Response({
            "sponsors": sponsors,
            "students": students
        })


class PaymentTypeApi(ListAPIView):
    model = PaymentType
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()
