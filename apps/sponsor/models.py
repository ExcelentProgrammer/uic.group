from django.db import models

from apps.base.models import PaymentType
from apps.student.models import Student
from django.utils.translation import gettext_lazy as _


class Sponsor(models.Model):
    STATUS = (
        (1, "Yangi"),
        (2, "Modernarsiyada"),
        (3, "Tasdiqlangan"),
        (4, "Bekor qilingan"),
    )

    full_name = models.CharField(max_length=255, verbose_name=_("full name"))
    phone = models.CharField(max_length=20, verbose_name=_("phone"))
    sum = models.BigIntegerField(verbose_name=_("summa"))
    payment_type = models.ManyToManyField(PaymentType, verbose_name=_("payment type"))
    firm = models.CharField(max_length=255, verbose_name=_("Firma"))
    is_legal = models.BooleanField(default=False, blank=True, null=True, verbose_name=_("is legal"))
    spent = models.BigIntegerField(verbose_name=_("spent"))
    created_at = models.DateTimeField(auto_now_add=True)
    get_status_display = models.IntegerField(default=STATUS[0][0], choices=STATUS, verbose_name=_("display status"))
    comment = models.TextField(blank=True, null=True, verbose_name=_("comment"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsor")


class SponsorTariff(models.Model):
    summa = models.BigIntegerField(verbose_name=_("summa"))

    class Meta:
        verbose_name = _("Sponsor tariff")
        verbose_name_plural = _("Sponsor tariff")
