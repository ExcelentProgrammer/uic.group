from rest_framework import serializers

from apps.sponsor.serializers import SponsorSerializer
from apps.sponsor_summa.models import SponsorSumma
from apps.student.serializers import StudentSerializer


class SponsorSummaSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer()
    student = StudentSerializer()

    class Meta:
        model = SponsorSumma
        fields = [
            "id",
            "sponsor",
            "summa",
            "student",
        ]


class SponsorSummaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorSumma
        fields = [
            "id",
            "sponsor",
            "summa",
            "student",
        ]
