from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.sponsor.models import Sponsor, SponsorTariff


# Register your models here.
class SponsorAdmin(ModelAdmin):
    list_display = [
        "full_name",
        "phone",
        "sum",
        "firm",
        "created_at"
    ]
    search_fields = [
        "full_name",
        "phone",
        "sum",
        "firm",
        "created_at"
    ]


class SponsorTariffAdmin(ModelAdmin):
    list_display = ['summa']
    search_fields = ['summa']


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorTariff, SponsorTariffAdmin)
