from singup.models import Member
from rest_framework import serializers
from django.contrib.auth.models import User


class MemberSerializer(serializers.ModelSerializer):
    class  Meta:
       model=Member
       fields=['firstname','lastname','Email','password']



class ChangePasswordSerializer(serializers.Serializer):
    model = Member

    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)       