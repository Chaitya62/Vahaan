from django.shortcuts import render
from django.http import HttpResponse
from .models import PUC
from login.models import VehicleUser

# Create your views here.


def index(request):

	return HttpResponse('Hello, World!')



def get_data(request):

	if request.method == 'POST':

		vehicle_id = request.POST.get('vehicle_id', '')

		vuser = VehicleUser.objects.get(id=vehicle_id)

		puc = PUC.objects.get(id=vehicle_id)

		return HttpResponse("sucuess")


	else:

		return HttpResponse('Wrong Page')