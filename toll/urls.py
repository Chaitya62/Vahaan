from django.urls import path, re_path, include
from .views import show_toll, get_toll_id, add_toll, search, consume_toll

urlpatterns = [
	re_path(r'^view_toll/(?P<id>[0-9]+)/$', show_toll, name = "view_toll"),
	re_path(r'^toll/(?P<id>[0-9]+)/$', get_toll_id, name = "toll"),
	re_path(r'^payments/', include('djstripe.urls', namespace="djstripe")),
	re_path(r'^add_toll/$', add_toll, name = "addToll"),
	re_path(r'^search_toll/$', search, name = "searchToll"),
	re_path(r'^consume/(?P<id>[0-9]+)/$', consume_toll, name = "consumeToll"),
]
