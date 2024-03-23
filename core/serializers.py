from rest_framework import serializers
from django.utils import timezone

from core.models import BaseModel

BASE_SERIALIZER_FIELDS = [
    field.name
    for field in BaseModel._meta.fields
]

class BaseSerializer(serializers.Serializer):
    created_by = serializers.HiddenField(
        default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault())
    )
    updated_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    # created_at = serializers.HiddenField(
    #     default=serializers.CreateOnlyDefault(timezone.now())
    # )
    # updated_at = serializers.HiddenField(
    #     default=timezone.now()
    # )
