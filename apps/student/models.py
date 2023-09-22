from django.db import models

from apps.institute.models import Institute
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Student(models.Model):
    TYPE = (
        (1, "Bakalavr"),
        (2, "Magistr"),
        (3, "Phd"),
    )

    STATUS = (
        (1, "Yangi"),
        (2, "Modernarsiyada"),
        (3, "Tasdiqlangan"),
        (4, "Bekor qilingan"),
    )

    full_name = models.CharField(max_length=255, verbose_name=_("full name"))
    type = models.IntegerField(choices=TYPE, verbose_name=_("type"))
    phone = models.CharField(max_length=255, verbose_name=_("phone"))
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name=_("institute"))
    contract = models.BigIntegerField(null=True, blank=True, verbose_name=_("contract"))
    given = models.BigIntegerField(null=True, blank=True, verbose_name=_("given"))
    get_status_display = models.IntegerField(default=STATUS[0][0], choices=STATUS, verbose_name=_("display status"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Student")
