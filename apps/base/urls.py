from django.urls import path

from apps.base.views import FaqListApi, DashboardApi, PaymentTypeApi

urlpatterns = [
    path("faq/", FaqListApi.as_view(),name="faq"),
    path("dashboard/", DashboardApi.as_view(),name="dashboard"),
    path("payment-type-list/", PaymentTypeApi.as_view(),name="payment-type"),
]
