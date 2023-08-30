from django.urls import path

from apps.student.views import StudentApi, StudentDeleteApi, StudentListApi, StudentUpdateApi, StudentDetailApi, \
    StudentSponsorApi

urlpatterns = [
    path("student-create/", StudentApi.as_view()),
    path("student-delete/<int:id>/", StudentDeleteApi.as_view()),
    path("student-detail/<int:id>/", StudentDetailApi.as_view()),
    path("student-list/", StudentListApi.as_view()),
    path("student-update/<int:id>/", StudentUpdateApi.as_view()),
    path("student-sponsor/<int:id>/", StudentSponsorApi.as_view()),

]
