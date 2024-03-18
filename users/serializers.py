from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core.serializers import BASE_SERIALIZER_FIELDS, BaseSerializer
from users.models import User


class UserSerializer(BaseSerializer, serializers.ModelSerializer):

    def to_internal_value(self, data):
        password = data.get('password', None)
        if password is not None:
            data['password'] = make_password(password)
        
        return super().to_internal_value(data)
    
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'is_staff',
            'cpf',
            'date_of_birth',
            'name',
            *BASE_SERIALIZER_FIELDS,
        ]
        extra_kwargs = {
            'is_staff': {'read_only': True},
            'password': {'read_only': True}
        }
    