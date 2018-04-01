from django.db import models
from login.models import AadharUser, VehicleUser

# Create your models here.

class Toll(models.Model):

	name = models.CharField(max_length = 255)
	location = models.CharField(max_length = 255)
	amount_vehicle_car = models.IntegerField()
	amount_vehicle_truck = models.IntegerField()
	amount_vehicle_lcv = models.IntegerField()
	amount_vehicle_3axel = models.IntegerField()
	amount_vehicle_4to6axel = models.IntegerField()
	amount_vehicle_7axel = models.IntegerField()
	amount_vehicle_hcm = models.IntegerField()

	class Meta:
		unique_together = ('name', 'location')

class TollPayment(models.Model):

	vehicle = models.ForeignKey(VehicleUser, on_delete = models.CASCADE)
	amount = models.IntegerField()
	date = models.DateField()
