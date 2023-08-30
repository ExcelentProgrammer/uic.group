from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.base.models import Faq, Dashboard, PaymentType


class FaqAdmin(ModelAdmin):
    list_display = ['question', 'answer']
    search_fields = ["question", 'answer']


class DashboardAdmin(ModelAdmin):
    list_display = [
        "total_income",
        "need",
        "other",
    ]
    search_fields = [
        "total_income",
        "need",
        "other",
    ]


class PaymentTypeAdmin(ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


admin.site.register(Faq, FaqAdmin)
admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
