from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from puc.models import PUC
import json
from .models import VehicleUser
import datetime
from django.views.decorators.csrf import csrf_exempt
from .sms_script import SMSClient
import loginapp.settings as settings



def set_cookie(response, key, value, days_expire = 7):
  if days_expire is None:
    max_age = 365 * 24 * 60 * 60  #one year
  else:
    max_age = days_expire * 24 * 60 * 60 
  expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value, max_age=max_age, expires=expires, domain=None, secure=None)



def is_logged(request):

	return request.user.is_authenticated



items = ['Home', 'Profile'];

def index(request):

	# if not is_logged(request):
	# 	return HttpResponse('Please login!')
	isAdmin = request.session.get('isAdmin', False)

	return render(request,'login/home.html',{'loggedin': is_logged(request),'isAdmin': isAdmin,'message': 'Hello, World!', 'title': 'HOME', 'items': items})




def adminhome(request):

	return render(request, 'login/admin_home.html')


class Login(View):
	



	def get(self,request):
		
		# checking here to avoid redirect recursion in middleware
		if request.user.is_authenticated:
			return HttpResponseRedirect('/home/')

		

		return render(request, 'login/login.html',{'message': 'from login', 'title':'login'})


	def post(self, request):

		


		username = request.POST.get('username',"")
		password = request.POST.get('password', "")
		admin = request.POST.get('stuff', "")


		user = authenticate(username=username, password=password)







		if user is None:
			return HttpResponse('Login failed')

		
		login(request, user)


		if admin == "":

			vuser = VehicleUser.objects.get(user=user)

			response = HttpResponseRedirect('/home/')

			set_cookie(response,'reg_no', vuser.reg_no)
			set_cookie(response,'username', vuser.user.username)
			set_cookie(response,'vehicle_type',vuser.vehicle_type)
			set_cookie(response,'user_id', vuser.user.id)
			set_cookie(response, 'vehicle_id',vuser.id)




			print("I WAS HERE")
			request.session['isAdmin'] = False

			return response
		else:
			request.session['isAdmin'] = True
				

		return HttpResponseRedirect('/home/')






class Logout(View):

	def get(self, request):

		logout(request)
		request.session['logged'] = False

		return HttpResponseRedirect('/login/')



@csrf_exempt
def get_user(request):

	if request.method == 'POST':

		reg_no = request.POST.get('reg_no', '')

		vuser = VehicleUser.objects.get(reg_no=reg_no)

		data = dict()

		data['username'] = vuser.user.username
		data['vehicle_id'] = vuser.id

		TODAY = datetime.datetime.today()

		puc = PUC.objects.filter(endDate__lte=TODAY)


		if len(puc) == 0:
			data['pucPending'] = 'false' 
		else:
			data['pucPeding'] = 'true'

	
	
		return HttpResponse(json.dumps(data))







class Signup(View):

	def post(self, request):


		username = request.POST.get('username',"")
		password = request.POST.get('password', "")
		cpassword = request.POST.get('cpassword', "")
		vehical_type = request.POST.get('vechical-type', "")
		UID = request.POST.get('aadhar', "")
		phone = request.POST.get('phone',"")






		VehicleUser = VehicleUser(username=username, password=password, vehical_type=vechical_type, UID=UID, phoneNumber=phone)



		


		user = User.objects.create_user(username, username+"@gmail.com", password)

		user.save()

		smsClient = SMSClient('9029168990', 'chaitya6262')

		smsClient.send(phoneNumber,'','Your Vahaan : username is '+username+' and  password is '+password)

		return HttpResponseRedirect('/login/')


# Create your views here.
