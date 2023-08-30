from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.student.models import Student


# Register your models here.
class StudentAdmin(ModelAdmin):
    list_display = ['full_name']
    search_fields = ['full_name']


admin.site.register(Student, StudentAdmin)
