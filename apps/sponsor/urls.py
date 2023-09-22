from django.urls import path

from apps.sponsor.views import SponsorCreateApi, SponsorDeleteApi, SponsorDetailApi, SponsorListApi, SponsorUpdateApi, \
    SponsorTariffApi

urlpatterns = [
    path("sponsor-create/", SponsorCreateApi.as_view(), name="create"),
    path("sponsor-delete/<int:id>/", SponsorDeleteApi.as_view(), name="delete"),
    path("sponsor-detail/<int:id>/", SponsorDetailApi.as_view(), name="detail"),
    path("sponsor-list/", SponsorListApi.as_view(), name="sponsor-list"),
    path("sponsor-update/<int:pk>/", SponsorUpdateApi.as_view(), name='update'),
    path("tariff-list/", SponsorTariffApi.as_view(), name="list"),
]
