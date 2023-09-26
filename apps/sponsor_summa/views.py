from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.sponsor_summa.models import SponsorSumma
from apps.sponsor_summa.serializers import SponsorSummaSerializer


class SponsorSummaViewSet(ModelViewSet):
    """Sponsor Summa View Set"""

    queryset = SponsorSumma.objects.all()
    serializer_class = SponsorSummaSerializer
    filterset_fields = ["sponsor"]

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
