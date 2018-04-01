from django.db import models

# Create your models here.


# class User(models.Model):
# 	username = models.CharField(max_length=55)
# 	password = models.CharField(max_length=55)
# 	social_media_id = models.CharField(max_length=55)
# 	social_media = models.CharField(max_length=55)



class AadharUser(models.Model):

	aadharN = models.CharField(max_length=55)	
	phoneNumber = models.CharField(max_length=55)




class VehicalUser(models.Model):

	VEHICAL_TYPE_CHOICES = (
		('CAR','CAR\\Jeep\\Van'),
		('LCV', 'LCV'),
		('BUS', 'BUS\\TRUCK'),
		('HCM\\EME','HCM\\EME'),
		('UPTO3AXLE', 'upto 3 axel'),
		('4-6 AXLE', '4 to 6 axel'),
		('7AXLE+', '7 axle or above')
	)

	reg_no = models.CharField(max_length=55)
	vehical_type = models.CharField(max_length=55, choices=VEHICAL_TYPE_CHOICES)
	UID = models.ForeignKey(AadharUser, on_delete=models.CASCADE)


	