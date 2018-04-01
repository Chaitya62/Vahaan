from django.urls import path, re_path
from .views import index, Login, Logout, Signup, adminhome, get_user, get_user_profile

urlpatterns = [
	re_path(r'login/$', Login.as_view(), name='login'),
	re_path(r'home/$', index, name='home'),
	re_path(r'logout/$', Logout.as_view(), name='logout'),
	re_path(r'signup/$', Signup.as_view(), name='signup'),
	re_path(r'adminhome/$',adminhome, name='adminhome'),
	re_path(r'get/user/$', get_user, name='get_user'),
	re_path(r'user/(?P<user>[a-zA-Z0-9]+)', get_user_profile, name='user_profile')
]