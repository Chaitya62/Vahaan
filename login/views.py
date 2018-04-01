from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
#from .sms_script import SMSClient



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

		login(request, user)

		if admin == "":


			print("I WAS HERE")
			request.session['isAdmin'] = False

			if user is None:
				return HttpResponse('Login failed')


		else:


			request.session['isAdmin'] = True
				

		return HttpResponseRedirect('/home/')






class Logout(View):

	def get(self, request):

		logout(request)
		request.session['logged'] = False

		return HttpResponseRedirect('/login/')







class Signup(View):

	def post(self, request):


		username = request.POST.get('username',"")
		password = request.POST.get('password', "")
		cpassword = request.POST.get('cpassword', "")

		


		user = User.objects.create_user(username, username+"@gmail.com", password)

		user.save()

		#smsClient = SMSClient('9029168990', 'chaitya6262')

		#smsClient.send('','Thanks for registering'+username+' your password is '+password)

		return HttpResponseRedirect('/login/')


# Create your views here.
