from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom User Model"""

    class Meta(AbstractUser.Meta):
        verbose_name = _("User")
        verbose_name_plural = _("User")
