from django.urls import path

from apps.student.views import StudentApi, StudentDeleteApi, StudentListApi, StudentUpdateApi, StudentDetailApi, \
    StudentSponsorApi

app_name = 'student'
urlpatterns = [
    path("student-create/", StudentApi.as_view(),name="create"),
    path("student-delete/<int:id>/", StudentDeleteApi.as_view(),name="delete"),
    path("student-detail/<int:id>/", StudentDetailApi.as_view(),name="detail"),
    path("student-list/", StudentListApi.as_view(),name="list"),
    path("student-update/<int:id>/", StudentUpdateApi.as_view(),name="update"),
    path("student-sponsor/<int:id>/", StudentSponsorApi.as_view(),name="sponsor"),

]
