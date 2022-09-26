from singup.models import Member
from singup.api.serializers import MemberSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated  


class myViewSet(viewsets.ModelViewSet):
    queryset=Member.objects.all()
    serializer_class=MemberSerializer

   

class ChangePasswordView(generics.UpdateAPIView):
    
    serializer_class = ChangePasswordSerializer
    model = Member
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.Member
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    