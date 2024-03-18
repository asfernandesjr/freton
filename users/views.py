from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import User
from .serializers import UserSerializer


class UserCreateApi(APIView):
    
    def post(self, request):
        serializer = UserSerializer(User.objects.all(), context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    

class UserListApi(APIView):
    authentication_classes = [authentication.BasicAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request, format=None):
        serializer = UserSerializer(User.objects.all(), many=True)
        
        return Response(serializer.data)