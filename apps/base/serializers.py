from rest_framework import serializers

from apps.base.models import Faq, Dashboard, PaymentType


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = [
            "id",
            "question",
            "answer"
        ]


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = [
            "total_income",
            "need",
            "other",
        ]


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = [
            "id",
            "title",
        ]
