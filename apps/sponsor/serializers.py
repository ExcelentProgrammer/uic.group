from rest_framework import serializers
from apps.base.models import PaymentType
from apps.base.serializers import PaymentTypeSerializer
from apps.sponsor.models import Sponsor, SponsorTariff


class SponsorSerializer(serializers.ModelSerializer):
    """Sponsor Serializer"""

    payment_type = PaymentTypeSerializer(many=True, read_only=True)
    payment = serializers.PrimaryKeyRelatedField(many=True, source="payment_type",
                                                 queryset=PaymentType.objects.all(), write_only=True)

    class Meta:
        read_only_fields = ['is_legal', "get_status_display"]
        model = Sponsor
        fields = [
            "id", "full_name",
            "phone", "sum",
            "payment", "payment_type", "firm",
            "spent", "comment",
            "is_legal", "created_at",
            "get_status_display"
        ]


class SponsorTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorTariff
        fields = ["summa"]
