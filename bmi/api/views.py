from bmi.models import User
from bmi.api.serializers import UserSerializer
from rest_framework import viewsets


class userewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

   

 