from django.urls import path

from apps.sponsor.views import SponsorCreateApi, SponsorDeleteApi, SponsorDetailApi, SponsorListApi, SponsorUpdateApi, \
    SponsorTariffApi

urlpatterns = [
    path("sponsor-create/", SponsorCreateApi.as_view()),
    path("sponsor-delete/<int:id>/", SponsorDeleteApi.as_view()),
    path("sponsor-detail/<int:id>/", SponsorDetailApi.as_view()),
    path("sponsor-list/", SponsorListApi.as_view()),
    path("sponsor-update/<int:pk>/", SponsorUpdateApi.as_view()),
    path("tariff-list/", SponsorTariffApi.as_view()),
]
