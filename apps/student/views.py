from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.student.models import Student
from apps.student.serializers import StudentSerializer, StudentSponsorSerializer


class StudentViewSet(ModelViewSet):
    """Student View Set"""

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['full_name']
    filterset_fields = ["get_status_display"]


class StudentSponsorApi(RetrieveAPIView):
    """Student Sponsor Detail Api View"""

    queryset = Student.objects.order_by("id")
    serializer_class = StudentSponsorSerializer
    lookup_url_kwarg = "id"
