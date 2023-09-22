from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as UAdmin

from apps.accounts.models import User


# Register your models here.
class UserAdmin(ModelAdmin):
    fieldsets = UAdmin.fieldsets
    list_display = ['username', "first_name", "last_name"]


admin.site.register(User, UserAdmin)
