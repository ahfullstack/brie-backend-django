from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(null=True, blank=True,max_length=32)
    description = models.CharField(null=True, blank=True,max_length=200)
    symptoms = ArrayField(ArrayField(models.IntegerField()))