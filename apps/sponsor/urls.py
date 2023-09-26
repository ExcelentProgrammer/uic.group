from django.urls import path

from apps.sponsor.views import SponsorTariffApi

urlpatterns = [
    path("tariff-list/", SponsorTariffApi.as_view(), name="list"),
]
