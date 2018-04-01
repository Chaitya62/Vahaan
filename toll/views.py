from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .serializers import TollPaymentSerializer, TollSerializer
from .models import TollPayment, Toll
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

def consume_toll(request, id):
	tollPayment = TollPayment.objects.filter(id = id, consumed = False)[0]
	tollPayment.consumed = True
	tollPayment.save()
	return HttpResponseRedirect("/home/")

@csrf_exempt
def search(request):
	searchString = request.POST.get('search', "");
	serializer = TollSerializer(Toll.objects.filter(name__icontains=searchString), many = True)
	content = JSONRenderer().render(serializer.data)
	return HttpResponse(content)

@csrf_exempt
def add_toll(request):

	if request.method == 'POST':
		tollPayment = TollPayment()
		tollPayment.vehicle_id = request.POST.get('vehicle_id', -1)
		tollPayment.toll_id = request.POST.get('toll_id', -1)
		print(tollPayment.vehicle_id)
		print(tollPayment.toll_id)
		tollPayment.amount = getTollAmount(tollPayment.vehicle_id, tollPayment.toll_id)


		tollPayment.date = request.POST.get('date', -1)
		
		print(tollPayment.date)

		tollPayment.save()
		return HttpResponseRedirect("/home/")



	else:


		tolls = Toll.objects.all()

		return render(request, 'toll/pay_toll.html',{'tolls': tolls})