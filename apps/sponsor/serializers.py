from rest_framework import serializers

from apps.base.serializers import PaymentTypeSerializer
from apps.sponsor.models import Sponsor, SponsorTariff


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            "id",
            "full_name",
            "phone",
            "sum",
            "payment_type",
            "firm",
            "spent",
            "comment",
            "created_at",
            "get_status_display"
        ]

        extra_kwargs = {
            "get_status_display": {"read_only": True},
            "firm": {"label": "Firma nomi"},
            "sum": {'label': "Summa"},
            "payment_type": {"label": "To'lov turi"},
            "phone": {"label": "Telefon raqam"},
            "full_name": {"label": "To'liq ism"},
            "spent": {"label": "Ishlatilgan summa"},
        }


class SponsorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            "id",
            "full_name",
            "phone",
            "sum",
            "is_legal",
            "firm",
            "comment",
            "created_at",
            "get_status_display",
        ]


class SponsorListSerializer(serializers.ModelSerializer):
    payment_type = PaymentTypeSerializer(many=True)

    class Meta:
        model = Sponsor
        fields = [
            "id",
            "full_name",
            "phone",
            "sum",
            "payment_type",
            "firm",
            "spent",
            "created_at",
            "get_status_display",
            "comment",
        ]


class SponsorTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorTariff
        fields = ["summa"]
