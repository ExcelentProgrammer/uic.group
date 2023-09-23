from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        verbose_name = _("User")
        verbose_name_plural = _("User")