from django.contrib import admin
from .models import Toll, TollPayment
# Register your models here.
admin.site.register([Toll, TollPayment])