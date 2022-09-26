from asyncio.windows_events import NULL
from django.db import models

# Create your models here.



class User(models.Model):
    FullName = models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    height = models.FloatField(default = NULL)
    Weight = models.FloatField(default = NULL)
    BMI_Calculate = models.FloatField(default = NULL)