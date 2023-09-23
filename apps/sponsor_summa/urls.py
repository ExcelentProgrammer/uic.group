from django.urls import path

from apps.sponsor_summa.views import SponsorSummaApi, SponsorSummaDeleteApi, SponsorSummaListApi, SponsorSummaUpdateApi

app_name = 'sponsor-summa'

urlpatterns = [
    path("sponsor-summa-create/", SponsorSummaApi.as_view(),name="create"),
    path("sponsor-summa-delete/<int:id>/", SponsorSummaDeleteApi.as_view(),name="delete"),
    path("sponsor-summa-list/", SponsorSummaListApi.as_view(),name="list"),
    path("sponsor-summa-update/<int:id>/", SponsorSummaUpdateApi.as_view(),name="update"),

]
