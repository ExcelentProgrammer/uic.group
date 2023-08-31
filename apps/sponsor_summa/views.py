from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView

from apps.sponsor_summa.models import SponsorSumma
from apps.sponsor_summa.serializers import SponsorSummaSerializer


# Create your views here.
class SponsorSummaApi(CreateAPIView):
    queryset = SponsorSumma.objects.all()
    serializer_class = SponsorSummaSerializer


class SponsorSummaDeleteApi(DestroyAPIView):
    queryset = SponsorSumma.objects.all()
    lookup_url_kwarg = "id"


class SponsorSummaListApi(ListAPIView):
    queryset = SponsorSumma.objects.all()
    serializer_class = SponsorSummaSerializer
    filterset_fields = ["sponsor"]


class SponsorSummaUpdateApi(UpdateAPIView):
    queryset = SponsorSumma.objects.all()
    serializer_class = SponsorSummaSerializer
    lookup_url_kwarg = "id"
