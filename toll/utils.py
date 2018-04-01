from .models import Toll
from login.models import VehicleUser

def getTollAmount(vehicle_id, toll_id):
	type = VehicleUser.objects.all().get(id = int(vehicle_id)).vehicle_type
	toll = Toll.objects.all().get(id = toll_id)
	if type == 'CAR':
		return toll.amount_vehicle_car
	if type == 'LCV':
		return toll.amount_vehicle_lcv
	if type == 'BUS':
		return toll.amount_vehicle_truck
	if type == 'UPTO3AXLE':
		return toll.amount_vehicle_3axel
	if type == '4-6 AXLE':
		return toll.amount_vehicle_4to6axel
	if type == '7AXLE+':
		return toll.amount_vehicle_7axel
	if type == 'HCM\\EME':
		return toll.amount_vehicle_hcm

	return -1
