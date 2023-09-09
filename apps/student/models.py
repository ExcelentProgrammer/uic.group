from django.db import models

from apps.institute.models import Institute


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

    full_name = models.CharField(max_length=255)
    type = models.IntegerField(choices=TYPE)
    phone = models.CharField(max_length=255)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    contract = models.BigIntegerField(null=True,blank=True)
    given = models.BigIntegerField(null=True,blank=True)
    get_status_display = models.IntegerField(default=STATUS[0][0], choices=STATUS)

    def __str__(self):
        return self.full_name
