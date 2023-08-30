from django.urls import path

from apps.sponsor_summa.views import SponsorSummaApi, SponsorSummaDeleteApi, SponsorSummaListApi, SponsorSummaUpdateApi

urlpatterns = [
    path("sponsor-summa-create/", SponsorSummaApi.as_view()),
    path("sponsor-summa-delete/<int:id>/", SponsorSummaDeleteApi.as_view()),
    path("sponsor-summa-list/", SponsorSummaListApi.as_view()),
    path("sponsor-summa-update/<int:id>/", SponsorSummaUpdateApi.as_view()),

]
