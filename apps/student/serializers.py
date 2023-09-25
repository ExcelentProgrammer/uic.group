from rest_framework import serializers

from apps.institute.models import Institute
from apps.institute.serializers import InstituteSerializer
from apps.student.models import Student


class StudentSerializer(serializers.ModelSerializer):

    """Student Serializer"""

    institute = InstituteSerializer(read_only=True)
    institute_id = serializers.PrimaryKeyRelatedField(source="institute", queryset=Institute.objects.all(),
                                                      write_only=True)
    type_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        read_only_fields = ['get_status_display']
        fields = [
            "id", "full_name",
            "type", "phone",
            "institute", "contract",
            "given", "get_status_display",
            "institute_id", "type_name"
        ]
        extra_kwargs = {
            "type": {"write_only": True}
        }

    def get_type_name(self, obj):
        return obj.get_type_display()


class StudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "full_name", "given",
            "get_status_display"
        ]
