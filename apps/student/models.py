from django.db import models

from apps.institute.models import Institute


# Create your models here.
class Student(models.Model):
    TYPE = (
        (1, "Bakalavr"),
        (2, "Magistr"),
        (3, "Phd"),
    )

    full_name = models.CharField(max_length=255)
    type = models.IntegerField(max_length=255, choices=TYPE)
    phone = models.CharField(max_length=255)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    contract = models.BigIntegerField()
    given = models.BigIntegerField()
    get_status_display = models.CharField(max_length=255, blank=True, null=True, default="Yangi")

    def __str__(self):
        return self.full_name
