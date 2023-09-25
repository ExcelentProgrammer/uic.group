from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView

from apps.sponsor.models import Sponsor, SponsorTariff
from apps.sponsor.serializers import SponsorSerializer, SponsorTariffSerializer


# Create your views here.
class SponsorCreateApi(CreateAPIView):
    queryset = Sponsor.objects.order_by("id")
    serializer_class = SponsorSerializer


class SponsorDeleteApi(DestroyAPIView):
    lookup_url_kwarg = 'id'
    queryset = Sponsor.objects.order_by("id")


class SponsorDetailApi(RetrieveAPIView):
    lookup_url_kwarg = "id"
    queryset = Sponsor
    serializer_class = SponsorSerializer


class SponsorListApi(ListAPIView):
    queryset = Sponsor.objects.order_by("id")
    serializer_class = SponsorSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = "__all__"


class SponsorUpdateApi(UpdateAPIView):
    queryset = Sponsor.objects.order_by("id")
    serializer_class = SponsorSerializer
    lookup_url_kwarg = "id"


class SponsorTariffApi(ListAPIView):
    queryset = SponsorTariff.objects.order_by("id")
    serializer_class = SponsorTariffSerializer
