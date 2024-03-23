from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from core.models import BaseModel
from users.models import User


class FreightStatus(models.TextChoices):
    IN_TRANSIT = _('In transit')
    PENDING = _('Pending')
    FINISHED = _('Finished')


class Vehicle(BaseModel):
    bus_number = models.CharField(_('bus number'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    capacity = models.PositiveIntegerField(_('capacity'))
    manufacturer = models.CharField(_('manufacturer'), max_length=100)
    model = models.CharField(_('model'), max_length=100)
    year = models.PositiveIntegerField(_('year'))
    
    def __str__(self) -> str:
        return self.bus_number
    
    class Meta:
        verbose_name = _('Vehicle')
        verbose_name_plural = _('Vehicles')
        ordering = ('bus_number',)
    
    
class Location(models.Model):
    address = models.TextField(_('address'))
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self) -> str:
        return f'{self.longitude},{self.latitude} - {self.address[:25]}'
    
    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')
        ordering = ('address',)
    
    
class Freight(BaseModel):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    driver = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    # crew = models.ManyToManyField(Driver)
    
    departure_location = models.ForeignKey(Location, related_name='departure_freight', on_delete=models.PROTECT)
    departure_datetime = models.DateTimeField(_('departure date and time'))
    
    destination_location = models.ForeignKey(Location, related_name='destination_freight', on_delete=models.PROTECT)
    estimated_arrival_datetime = models.DateTimeField(_('estimated arrival date and time'))
    
    status = models.CharField(_('status'), max_length=15, choices=FreightStatus.choices)
    finished_datetime = models.DateTimeField(_('finished date and time'), null=True, blank=True)

    distance = models.PositiveIntegerField(_('distance (km)'), null=True)
    price = models.DecimalField(_('price'), max_digits=6, decimal_places=2)


    def __str__(self) -> str:
        return f'[{self.status}] {self.departure_datetime} - \
            {self.finished_datetime if self.status == FreightStatus.FINISHED else self.estimated_arrival_datetime}'
    
    class Meta:
        verbose_name = _('Freight')
        verbose_name_plural = _('Freights')
        ordering = ('departure_datetime',)
            
            
# class FreightOccurrence(BaseModel):
#     name = models.CharField(_('name'), max_length=100)
#     description = models.TextField(_('description'))
#     location = models.ForeignKey(Location, null=True)
#     datetime = models.DateTimeField(default=timezone.now)
    
#     freight = models.ForeignKey(Freight)
    
#     def __str__(self) -> str:
#         return self.name