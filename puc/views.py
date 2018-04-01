from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import PUC
from login.models import VehicleUser
from rest_framework.renderers import JSONRenderer
from .serializers import PUCSerializer
from django.views.decorators.csrf import csrf_exempt
from dateutil.relativedelta import relativedelta
import datetime

# Create your views here.


def index(request):
	return HttpResponse('Hello, World!')


@csrf_exempt
def get_data(request):

	if request.method == 'POST':


		vehicle_id = request.POST.get('vehicle_id', 1)

		vuser = VehicleUser.objects.get(id=int(vehicle_id))

		print(vuser.user.username)

		puc = PUC.objects.get(user=vuser)


		serializer = PUCSerializer(puc)
		content = JSONRenderer().render(serializer.data)

		
		return HttpResponse(content)



	else:

		response = HttpResponse("HEllo")

		return response



# def get_pending(request):

# 	if request.method == 'POST':



@csrf_exempt
def put_data(request):

	if request.method =='POST':

		months = request.POST.get('months', '3')
		vehicle_id = int(request.session.get('vehicle_id', 1))


		TODAY = datetime.date.today()

		month_offset = relativedelta(months=int(months))


		# month_id = 3;

		vuser = VehicleUser.objects.get(id=vehicle_id)

		PUC.objects.filter(user=vuser).delete()

		puc = PUC(user=vuser, months=months, endDate=(TODAY+month_offset))

		puc.save()
		return HttpResponseRedirect('/home/')

	else:

		return render(request, 'puc/create_puc.html',{'items': ['Home']})