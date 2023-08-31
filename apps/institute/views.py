from django.shortcuts import render
from rest_framework.generics import ListAPIView

from apps.institute.models import Institute
from apps.institute.serializers import InstituteSerializer


# Create your views here.
class InstituteListApi(ListAPIView):
    model = Institute
    serializer_class = InstituteSerializer
    queryset = Institute.objects.all()
    filterset_fields = ["name"]
