from django.shortcuts import render, HttpResponse
from .forms import CreateBookingForm
from django.http import  JsonResponse
from django.contrib.auth.models import User
from services.services import Check_availability
from listing.models import  Room
from .models import Request
# Create your views here.
def create_booking(request):
	form = CreateBookingForm()
	if request.method == 'POST':
		form = CreateBookingForm(request.POST)
		print(form.data)
		data = form.data
		if form.is_valid():
			available = Check_availability(data['place'],data['check_in'],data['check_out'])
			if available:
				form.save()
				place = Room.objects.get(id=data['place']) 
			else:
				form.save(commit=False)
				
		else:
			form = CreateBookingForm()



	return HttpResponse("Thank you " + " you booked " + place.name + " for " ) #JsonResponse(data, safe=False)

def list_bookings(request):
	return HttpResponse("")

def cancel_booking(request):
	return HttpResponse("")


def create_rent(request):
	return HttpResponse("")

def list_rents(request):
	return HttpResponse("")

def cancel_rent(request):
	return HttpResponse("")


def send_request(request, user_id,place_id):
	user = User.objects.get(id=user_id)
	place = Room.objects.get(id=place_id)
	if user != None and place != None:
		Request.objects.create(user=user,place=place,sent=True)

	return HttpResponse("request sent")
