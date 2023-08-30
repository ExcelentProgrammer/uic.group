from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.sponsor_summa.models import SponsorSumma


# Register your models here.

class SponsorSummaAdmin(ModelAdmin):
    list_display = [
        "sponsor",
        "summa",
        "student",
    ]
    search_fields = [
        "sponsor",
        "summa",
        "student",
    ]


admin.site.register(SponsorSumma, SponsorSummaAdmin)
