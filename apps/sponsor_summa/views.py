from django.db.models import Sum
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response

from apps.sponsor_summa.models import SponsorSumma
from apps.sponsor_summa.serializers import SponsorSummaSerializer, SponsorSummaCreateSerializer


# Create your views here.
class SponsorSummaApi(CreateAPIView):
    """Sponsor Summa Api View"""

    queryset = SponsorSumma.objects.order_by("id")
    serializer_class = SponsorSummaCreateSerializer

    def create(self, request, *args, **kwargs):
        """Custom create function"""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        student = data.get("student")
        sponsor = data.get("sponsor")

        if int(sponsor.get_status_display) != 3:
            # Xomiy Tasdiqlanmagan bo'lsa

            return Response(
                {"success": False, "message": "Xomiy Tasdiqlanmagan", "code": 1003,
                 "status": sponsor.get_status_display})

        summa = int(data.get("summa"))
        sponsor_summa = SponsorSumma.objects.filter(student=student).aggregate(total_amount=Sum('summa')).get(
            "total_amount", 0)

        sponsor_summa = 0 if sponsor_summa is None else sponsor_summa

        if sponsor_summa >= int(student.contract):
            # Talaba Kontrakti to'lab bo'lingan bo'lsa

            return Response({"success": False, "message": "Student contracti to'langan", "code": 1001})

        elif not int(sponsor.sum) >= summa:
            # Xomiyda pul yetarli bo'lmasa

            return Response(
                {"success": False, "message": "Sponsordagi pul yetarli emas", "code": 1002, "balance": sponsor.sum})

        sponsor.sum = int(sponsor.sum) - sponsor_summa
        sponsor.save()

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class SponsorSummaDeleteApi(DestroyAPIView):
    """Sponsor Summa Delete Api View"""

    queryset = SponsorSumma.objects.order_by("id")
    lookup_url_kwarg = "id"


class SponsorSummaListApi(ListAPIView):
    """Sponsor Summma List Api View"""

    queryset = SponsorSumma.objects.order_by("id")
    serializer_class = SponsorSummaSerializer
    filterset_fields = ["sponsor"]


class SponsorSummaUpdateApi(UpdateAPIView):
    """Sponsor Summa Update Api View"""

    queryset = SponsorSumma.objects.order_by("id")
    serializer_class = SponsorSummaSerializer
    lookup_url_kwarg = "id"
