from django.db.models import Count, F, Value
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.base.models import Faq, Dashboard, PaymentType
from apps.base.serializers import FaqSerializer, DashboardSerializer, PaymentTypeSerializer
from apps.sponsor.models import Sponsor


class FaqListApi(ListAPIView):
    model = Faq
    serializer_class = FaqSerializer
    queryset = Faq.objects.all()


class DashboardApi(APIView):

    def get(self, request):
        months = []

        for m in range(1, 13):
            month = Sponsor.objects.filter(created_at__month=m)
            if month.count() == 0:
                continue

            name = month.first().created_at.strftime("%B")
            months.append({
                "Label": name,
                "value": month.count()
            })
        return Response(months)


class PaymentTypeApi(ListAPIView):
    model = PaymentType
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()
