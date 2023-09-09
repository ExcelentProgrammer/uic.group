from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.base.models import Faq, PaymentType


class FaqAdmin(ModelAdmin):
    list_display = ['question', 'answer']
    search_fields = ["question", 'answer']


class PaymentTypeAdmin(ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


admin.site.register(Faq, FaqAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
