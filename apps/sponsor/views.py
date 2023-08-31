from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView

from apps.sponsor.models import Sponsor, SponsorTariff
from apps.sponsor.serializers import SponsorCreateSerializer, SponsorDetailSerializer, SponsorListSerializer, \
    SponsorTariffSerializer


# Create your views here.
class SponsorCreateApi(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer


class SponsorDeleteApi(DestroyAPIView):
    lookup_url_kwarg = 'id'
    queryset = Sponsor.objects.all()


class SponsorDetailApi(RetrieveAPIView):
    lookup_url_kwarg = "id"
    queryset = Sponsor
    serializer_class = SponsorDetailSerializer


class SponsorListApi(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorListSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = "__all__"


class SponsorUpdateApi(UpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer
    lookup_url_kwarg = "id"


class SponsorTariffApi(ListAPIView):
    queryset = SponsorTariff.objects.all()
    serializer_class = SponsorTariffSerializer

