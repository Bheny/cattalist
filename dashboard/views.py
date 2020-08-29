from django.shortcuts import render
from location.models import Area
# Create your views here.
def home(request):
	return render(request, 'dashboard/index.html', {})

def add_listing(request):
	areas = Area.objects.all()
	return render(request, 'dashboard/add_listing.html', {'areas':areas})


def add_room(request):
	areas = Area.objects.all()
	return render(request, 'dashboard/add_room.html', {'areas':areas})


def add_others(request):
	return render (request, 'dashboard/add_others.html', {})