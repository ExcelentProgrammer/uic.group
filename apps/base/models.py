from django.db import models


# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


class PaymentType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
