from rest_framework import serializers

from apps.institute.models import Institute


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = [
            "id",
            "name",
        ]
