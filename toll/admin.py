from django.contrib import admin

from .models import Toll, TollPayment

admin.site.register([Toll, TollPayment])