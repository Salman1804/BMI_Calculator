from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class Member(models.Model):
    Email=models.EmailField(max_length=100,default=NULL)
    password=models.CharField(max_length=12)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    

    