from django.shortcuts import render
from django.http import HttpResponse
from .serializers import TollPaymentSerializer
from .models import TollPayment
from rest_framework.renderers import JSONRenderer

# Create your views here.

def show_toll(request, id):
	serializer = TollPaymentSerializer(TollPayment.objects.filter(vehicle_id=id, consumed = False), many = True)
	content = JSONRenderer().render(serializer.data)
	return HttpResponse(content)

def get_toll_id(request, id):
	serializer = TollPaymentSerializer(TollPayment.objects.filter(id=id, consumed = False), many = True)
	content = JSONRenderer().render(serializer.data)
	# QR CODE ??
	return HttpResponse(content)
