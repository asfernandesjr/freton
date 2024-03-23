
from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework.views import exception_handler
from rest_framework.serializers import as_serializer_error
from rest_framework.response import Response
from rest_framework import status, exceptions


def django_validation_error_handler(exc, context):
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))
    
    response = exception_handler(exc, context)
    
    if response is None:
        return response
    
    if isinstance(exc.detail, (list, dict)):
        response.data = {
            "detail": response.data
        }
    
    return response