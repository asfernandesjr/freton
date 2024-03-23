from django.contrib import admin

from freight.models import Freight, Location, Vehicle

admin.site.register(Vehicle)
admin.site.register(Location)
admin.site.register(Freight)