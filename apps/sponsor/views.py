from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView

from apps.sponsor.models import Sponsor, SponsorTariff
from apps.sponsor.serializers import SponsorSerializer, SponsorTariffSerializer


class SponsorCreateApi(CreateAPIView):
    """Sponsor Create Api View"""

    queryset = Sponsor.objects.order_by("id")
    serializer_class = SponsorSerializer


class SponsorDeleteApi(DestroyAPIView):
    """Sponsor delete Api View"""

    lookup_url_kwarg = 'id'
    queryset = Sponsor.objects.order_by("id")


class SponsorDetailApi(RetrieveAPIView):
    """Sponsor Detail Api View"""

    lookup_url_kwarg = "id"
    queryset = Sponsor
    serializer_class = SponsorSerializer


class SponsorListApi(ListAPIView):
    """Sponsor List Api View"""

    queryset = Sponsor.objects.order_by("id")
    serializer_class = SponsorSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = "__all__"


class SponsorUpdateApi(UpdateAPIView):
    """Sponsor Update Api View"""

    queryset = Sponsor.objects.order_by("id")
    serializer_class = SponsorSerializer
    lookup_url_kwarg = "id"


class SponsorTariffApi(ListAPIView):
    """Sponsor Tariff Api View"""

    queryset = SponsorTariff.objects.order_by("id")
    serializer_class = SponsorTariffSerializer
