from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.sponsor.models import Sponsor, SponsorTariff
from apps.sponsor.serializers import SponsorSerializer, SponsorTariffSerializer


class SponsorViewSet(ModelViewSet):
    """Sponsor View Set"""

    queryset = Sponsor.objects.order_by("id")
    serializer_class = SponsorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['full_name']
    filterset_fields = ["get_status_display"]


class SponsorTariffApi(ListAPIView):
    """Sponsor Tariff Api View"""

    queryset = SponsorTariff.objects.order_by("id")
    serializer_class = SponsorTariffSerializer
