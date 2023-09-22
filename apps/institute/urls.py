from django.urls import path

from apps.institute.views import InstituteListApi

app_name = "institute"

urlpatterns = [
    path("institute-list/",InstituteListApi.as_view(),name="name")
]