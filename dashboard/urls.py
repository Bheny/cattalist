from django.urls import path
from .views import *

app_name = "dashboard"

urlpatterns = [
	path('', home,name='home'),
	path('add/listing/', add_listing, name="add_listing"),
	path('add/room/', add_room, name="add_room"),
	path('add/others/', add_others, name="add_others"),
]