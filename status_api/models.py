from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(null=True, blank=True,max_length=32)
    description = models.CharField(null=True, blank=True,max_length=200)
    feelings = models.IntegerField(default=0)
    worries = models.IntegerField(default=0)
    fears = models.IntegerField(default=0)
    troubles = models.IntegerField(default=0)
