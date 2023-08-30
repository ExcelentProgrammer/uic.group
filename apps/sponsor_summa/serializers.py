from rest_framework import serializers

from apps.sponsor_summa.models import SponsorSumma


class SponsorSummaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorSumma
        fields = [
            "id",
            "sponsor",
            "summa",
            "student",
        ]
