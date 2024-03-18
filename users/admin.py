from django.contrib import admin
from .models import User, DrivingCategory, DrivingLicense

admin.site.register(User)
admin.site.register(DrivingCategory)
admin.site.register(DrivingLicense)