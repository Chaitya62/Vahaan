from rest_framework import serializers
from .models import PUC

class PUCSerializer(serializers.ModelSerializer):

	class Meta:
		model =  PUC
		fields = ('startDate', 'months', 'done', 'endDate')
