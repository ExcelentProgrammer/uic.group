from django.urls import path

from apps.student.views import StudentSponsorApi

urlpatterns = [
    path("student-sponsor/<int:id>/", StudentSponsorApi.as_view(), name="sponsor"),
]
