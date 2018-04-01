from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class User(models.Model):
# 	username = models.CharField(max_length=55)
# 	password = models.CharField(max_length=55)
# 	social_media_id = models.CharField(max_length=55)
# 	social_media = models.CharField(max_length=55)



class AadharUser(models.Model):

	aadharN = models.CharField(max_length=55)	
	phoneNumber = models.CharField(max_length=55)




class VehicleUser(models.Model):

	VEHICLE_TYPE_CHOICES = (
		('CAR','CAR\\Jeep\\Van'),
		('LCV', 'LCV'),
		('BUS', 'BUS\\TRUCK'),
		('HCM\\EME','HCM\\EME'),
		('UPTO3AXLE', 'upto 3 axel'),
		('4-6 AXLE', '4 to 6 axel'),
		('7AXLE+', '7 axle or above')
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	reg_no = models.CharField(max_length=55, default=None)
	vehicle_type = models.CharField(max_length=55, choices=VEHICLE_TYPE_CHOICES)
	UID = models.CharField(max_length=55, default=None)
	phoneNumber = models.CharField(max_length=55, default="NULL")


