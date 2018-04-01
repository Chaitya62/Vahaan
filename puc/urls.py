from django.urls import path, re_path
from .views import index, get_data

urlpatterns = [
	re_path(r'puc/$', index, name='index'),
	re_path(r'puc/get/$',get_data, name='get')
]
