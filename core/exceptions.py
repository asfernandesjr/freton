
from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def django_validation_error_handler(exc, context):
    
    response = exception_handler(exc, context)
    
    if response is None and isinstance(exc, DjangoValidationError):
        return Response(data=exc.message_dict, status=status.HTTP_400_BAD_REQUEST)
    
    return response