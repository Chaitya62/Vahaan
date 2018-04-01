from django.contrib import admin

from .models import AadharUser, VehicleUser

# Register your models here.
admin.site.register([AadharUser, VehicleUser])