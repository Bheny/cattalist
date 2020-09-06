from django.shortcuts import render
from listing.models import Listing, Room
from location.models import Area
# Create your views here.
def home(request):
	print(request.POST)
	rooms = Room.objects.all()
	result = False 
	locations = Area.objects.all()
	if request.method == 'POST':
		Type = request.POST['type']
		location = request.POST['location']
		if location == "all":
			rooms = Room.objects.filter(max_quantity=Type)
			result = True
		else:
			rooms = Room.objects.filter(location=location).filter(max_quantity=Type)
			result = True


	return render(request, 'index.html',{'listings':rooms,'results':result,'areas':locations})



def about(request):
	return render(request, 'about.html', {})


