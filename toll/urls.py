from django.urls import path, re_path, include
from .views import show_toll, get_toll_id, add_toll

urlpatterns = [
	re_path(r'^view_toll/(?P<id>[0-9]+)/$', show_toll, name = "view_toll"),
	re_path(r'^toll/(?P<id>[0-9]+)/$', get_toll_id, name = "toll"),
	re_path(r'^payments/', include('djstripe.urls', namespace="djstripe")),
	re_path(r'^add_toll/$', add_toll, name = "addToll")
]
