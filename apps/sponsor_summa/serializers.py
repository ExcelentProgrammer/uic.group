from rest_framework import serializers

from apps.sponsor.models import Sponsor
from apps.sponsor.serializers import SponsorSerializer
from apps.sponsor_summa.models import SponsorSumma
from apps.student.models import Student
from apps.student.serializers import StudentSerializer


class SponsorSummaSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    sponsor_id = serializers.PrimaryKeyRelatedField(source="sponsor", queryset=Sponsor.objects.all())
    student_id = serializers.PrimaryKeyRelatedField(source="student", queryset=Student.objects.all())

    class Meta:
        model = SponsorSumma
        fields = [
            "id",
            "sponsor",
            "summa",
            "student",
            "sponsor_id",
            "student_id"
        ]


