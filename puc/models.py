from django.db import models

from login.models import VehicleUser
import datetime

# Create your models here.



class PUC(models.Model):


	user = models.ForeignKey(VehicleUser, on_delete=models.CASCADE)
	startDate = models.DateField(auto_now_add=True)
	months = models.CharField(max_length=55)
	endDate = models.DateField(default=datetime.datetime.now())
	done = models.CharField(max_length=55, default='true')
	
	# Can include cost maybe	

