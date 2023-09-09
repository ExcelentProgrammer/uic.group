from django.db import models

from apps.base.models import PaymentType
from apps.student.models import Student


class Sponsor(models.Model):
    STATUS = (
        (1, "Yangi"),
        (2, "Modernarsiyada"),
        (3, "Tasdiqlangan"),
        (4, "Bekor qilingan"),
    )

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    sum = models.BigIntegerField()
    payment_type = models.ManyToManyField(PaymentType)
    firm = models.CharField(max_length=255)
    is_legal = models.BooleanField(default=False, blank=True, null=True)
    spent = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    get_status_display = models.IntegerField(default=STATUS[0][0], choices=STATUS)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class SponsorTariff(models.Model):
    summa = models.BigIntegerField()
