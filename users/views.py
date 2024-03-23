from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from core.pagination import LimitOffsetPagination, get_paginated_response

from .models import User
from .serializers import UserSerializer


class UserCreateApi(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    

class UserListApi(APIView):
    authentication_classes = [authentication.BasicAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request, format=None):
        users_qs = User.objects.all()

        return get_paginated_response(
            pagination_class=LimitOffsetPagination,
            serializer_class=UserSerializer,
            queryset=users_qs,
            request=request,
            view=self
        )