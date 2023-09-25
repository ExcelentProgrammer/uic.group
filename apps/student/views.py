from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView

from apps.student.models import Student
from apps.student.serializers import StudentSerializer, StudentSponsorSerializer


class StudentApi(CreateAPIView):
    """Student Create Api View"""

    queryset = Student.objects.order_by("id")
    serializer_class = StudentSerializer


class StudentDeleteApi(DestroyAPIView):
    """Student Delete Api View"""

    queryset = Student.objects.order_by("id")
    lookup_url_kwarg = "id"


class StudentDetailApi(RetrieveAPIView):
    """Student Detail Api View"""

    queryset = Student.objects.order_by("id")
    lookup_url_kwarg = "id"
    serializer_class = StudentSerializer


class StudentListApi(ListAPIView):
    """Student List Api View"""

    queryset = Student.objects.order_by("id")
    serializer_class = StudentSerializer
    filterset_fields = ["get_status_display"]


class StudentUpdateApi(UpdateAPIView):
    """Student Update Api View"""

    queryset = Student.objects.order_by("id")
    serializer_class = StudentSerializer
    lookup_url_kwarg = "id"


class StudentSponsorApi(RetrieveAPIView):
    """Student Sponsor Detail Api View"""

    queryset = Student.objects.order_by("id")
    serializer_class = StudentSponsorSerializer
    lookup_url_kwarg = "id"
