from django.db import models

from apps.sponsor.models import Sponsor
from apps.student.models import Student


# Create your models here.
class SponsorSumma(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    summa = models.BigIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.sponsor.full_name
