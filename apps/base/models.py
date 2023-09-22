from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=255, verbose_name=_("question"))
    answer = models.TextField(verbose_name=_("answer"))

    class Meta:
        verbose_name = _("Faq")
        verbose_name_plural = _("Faq")


class PaymentType(models.Model):
    title = models.CharField(max_length=255,verbose_name=_("title"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Payment type")
        verbose_name_plural = _("Payment type")
