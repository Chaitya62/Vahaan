from django.urls import path, re_path
from .views import show_toll

urlpatterns = [
	re_path(r'^view_toll/(?P<id>[0-9]+)/$', show_toll, name = "view_toll"),
	re_path(r'^')
]
