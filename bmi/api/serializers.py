from bmi.models import User
from rest_framework import serializers
#from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class  Meta:
       model=User
       fields=['FullName','Gender','height','Weight','BMI_Calculate']



