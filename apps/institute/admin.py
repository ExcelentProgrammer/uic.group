from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.institute.models import Institute


class InstituteAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Institute, InstituteAdmin)
