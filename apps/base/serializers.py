from rest_framework import serializers

from apps.base.models import Faq, PaymentType


class FaqSerializer(serializers.ModelSerializer):
    """Ko'p so'raladigan savollar yani FAQ uchun serializer"""

    class Meta:
        model = Faq
        fields = [
            "id", "question",
            "answer"
        ]


class PaymentTypeSerializer(serializers.ModelSerializer):
    """Payment Type uchun serializer"""

    class Meta:
        model = PaymentType
        fields = [
            "id", "title",
        ]
