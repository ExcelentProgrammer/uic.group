from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = _("Faq")
        verbose_name_plural = _("Faq")


class PaymentType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Payment type")
        verbose_name_plural = _("Payment type")
