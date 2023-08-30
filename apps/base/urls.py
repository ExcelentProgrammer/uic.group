from django.urls import path

from apps.base.views import FaqListApi, DashboardApi, PaymentTypeApi

urlpatterns = [
    path("faq/", FaqListApi.as_view()),
    path("dashboard/", DashboardApi.as_view()),
    path("payment-type-list/", PaymentTypeApi.as_view()),
]
