from django.urls import path
from .views import *

app_name = 'listing'

urlpatterns = [
	path('<int:id>/<slug:slug>', room_detail, name="room_detail"),
]