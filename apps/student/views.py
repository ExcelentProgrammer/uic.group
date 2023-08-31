from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView

from apps.student.models import Student
from apps.student.serializers import StudentSerializer, StudentCreateSerializer, StudentSponsorSerializer


class StudentApi(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer


class StudentDeleteApi(DestroyAPIView):
    queryset = Student.objects.all()
    lookup_url_kwarg = "id"


class StudentDetailApi(RetrieveAPIView):
    queryset = Student.objects.all()
    lookup_url_kwarg = "id"
    serializer_class = StudentSerializer


class StudentListApi(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ["get_status_display"]


class StudentUpdateApi(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    lookup_url_kwarg = "id"


class StudentSponsorApi(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSponsorSerializer
    lookup_url_kwarg = "id"
