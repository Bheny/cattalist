from django.urls import path
from .views import *

app_name = 'listing'

urlpatterns = [
	path('api/all/', place_listings),
	path('<int:id>/<slug:slug>', room_detail, name="room_detail"),
	path('room_listing', setup, name="setup"),
]