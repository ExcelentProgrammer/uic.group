from django.db import models

from apps.sponsor.models import Sponsor
from apps.student.models import Student
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SponsorSumma(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, verbose_name=_("sponsor"))
    summa = models.BigIntegerField(verbose_name=_("summa"))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_("student"))

    def __str__(self):
        return self.sponsor.full_name

    class Meta:
        verbose_name = _("Sponsor summa")
        verbose_name_plural = _("Sponsor summa")
