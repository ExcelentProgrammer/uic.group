from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Institute(models.Model):
    name = models.CharField(max_length=255,verbose_name=_("name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Institute")
        verbose_name_plural = _("Institute")
     
