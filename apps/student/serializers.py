from rest_framework import serializers

from apps.institute.serializers import InstituteSerializer
from apps.student.models import Student


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        read_only_fields = ['get_status_display']
        fields = [
            "id",
            "full_name",
            "type",
            "phone",
            "institute",
            "contract",
            "given",
            "get_status_display",
        ]

        extra_kwargs = {
            "full_name": {"label": "To'liq ism"},
            "type": {"label": "O'quv tur"},
            "phone": {"label": "Telefon raqam"},
            "contract": {"label": "Kantrakt miqdori"},
            "given": {"label": "Berilgan summa"},
        }


class StudentSerializer(serializers.ModelSerializer):
    institute = InstituteSerializer()

    class Meta:
        model = Student
        read_only_fields = ['get_status_display']
        fields = [
            "id",
            "full_name",
            "type",
            "phone",
            "institute",
            "contract",
            "given",
            "get_status_display",
        ]


class StudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "full_name",
            "given",
            "get_status_display"
        ]
