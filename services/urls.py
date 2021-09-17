from django.urls import path
from .views import *

app_name = 'services'

urlpatterns = [
	path('', list_bookings, name='list_bookings'),
	path('create_booking/', create_booking, name="create_booking"),
	path('cancel_booking/', cancel_booking, name='cancel_booking'),
	path('rentals', list_rents, name='list_rents'),
	path('create_rent/', create_rent, name="create_rent"),
	path('cancel_rent/', cancel_rent, name='cancel_rent'),
	#==========================================================
	path('send_request/<int:user_id>/<int:place_id>/', send_request, name="send_request"),
]