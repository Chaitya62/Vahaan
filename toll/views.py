from django.shortcuts import render
from django.http import HttpResponse
from .serializers import TollPaymentSerializer
from .models import TollPayment
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .utils import getTollAmount

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

@csrf_exempt
def add_toll(request):

	if request.method == 'POST':
		tollPayment = TollPayment()
		tollPayment.vehicle_id = request.POST.get('vehicle_id', -1)
		tollPayment.toll_id = request.POST.get('toll_id', -1)
		tollPayment.amount = getTollAmount(tollPayment.vehicle_id, tollPayment.toll_id)
		tollPayment.date = request.POST.get('date', -1)
		tollPayment.save()
		return HttpResponse("Done")

	return HttpResponse("404 Not Found")