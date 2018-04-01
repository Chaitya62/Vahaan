from rest_framework import serializers
from .models import TollPayment, Toll

class TollSerializer(serializers.ModelSerializer):

	class Meta:
		model =  Toll
		fields = ('id', 'name', 'location', 'amount_vehicle_car', 'amount_vehicle_truck', 'amount_vehicle_lcv', 'amount_vehicle_3axel', 'amount_vehicle_4to6axel', 'amount_vehicle_7axel', 'amount_vehicle_hcm')

class TollPaymentSerializer(serializers.ModelSerializer):
	toll = TollSerializer(read_only = True)
	vehicle = serializers.PrimaryKeyRelatedField(read_only = True)

	class Meta:
		model = TollPayment
		fields = ('toll', 'vehicle', 'amount', 'date', 'consumed')
