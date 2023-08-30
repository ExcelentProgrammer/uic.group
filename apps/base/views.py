from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.base.models import Faq, Dashboard, PaymentType
from apps.base.serializers import FaqSerializer, DashboardSerializer, PaymentTypeSerializer


class FaqListApi(ListAPIView):
    model = Faq
    serializer_class = FaqSerializer
    queryset = Faq.objects.all()


class DashboardApi(APIView):

    def get(self, request):
        data = Dashboard.objects.all().order_by("id").reverse()

        if data.exists():
            response = DashboardSerializer(data.first())
            return Response(response.data)

        return Response({"success": False, "message": "dashboard.data.not.found"})


class PaymentTypeApi(ListAPIView):
    model = PaymentType
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()
