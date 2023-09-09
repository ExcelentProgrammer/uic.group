from rest_framework import serializers

from apps.base.models import Faq, PaymentType


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = [
            "id",
            "question",
            "answer"
        ]





class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = [
            "id",
            "title",
        ]
