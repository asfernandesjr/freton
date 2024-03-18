from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from core.models import BaseModel, CoreModel

from .validators import CPFValidator, DriverLicenseRegisterNumberValidator


class User(AbstractUser, BaseModel):
    password = models.CharField(_("password"), max_length=128, blank=True)
    name = models.CharField(_('name'), max_length=255)
    cpf = models.CharField(
        _('CPF'),
        max_length=11,
        unique=True,
        error_messages={
            'unique': _('A user with that CPF already exists.')
        },
        validators=[CPFValidator()],
    )
    date_of_birth = models.DateField(
        _('date of birth'),
        null=True,
        blank=True
    )
    
    # Removed fields from AbstractUser model
    first_name = None
    last_name = None
    date_joined = None
    
    REQUIRED_FIELDS = ['email', 'name', 'cpf', 'date_of_birth']
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('id',)


class DrivingCategory(CoreModel):
    category = models.CharField(
        _('category'),
        max_length=4,
    )
    description  = models.TextField(_('description'), blank=True)

    class Meta:
        verbose_name = _('Driving category')
        verbose_name_plural = _('Driving categories')
        ordering = ('category',)


class DrivingLicense(BaseModel):
    driver = models.OneToOneField(User, on_delete=models.CASCADE)
    register_number = models.CharField(
        _('register_number'),
        max_length=11,
        unique=True,
        validators=[DriverLicenseRegisterNumberValidator()],
    )
    issuance_date = models.DateField(
        _('issuance date'),
    )
    validity_date = models.DateField(
        _('validity date'),
    )
    categories = models.ManyToManyField(DrivingCategory)
    
    class Meta:
        verbose_name = _('Driving license')
        verbose_name_plural = _('Driving licenses')
        ordering = ('id',)
    
    