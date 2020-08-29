from django.shortcuts import render
from listing.models import Listing, Room

# Create your views here.
def home(request):
	rooms = Room.objects.all()
	listings = Listing.objects.all()
	return render(request, 'index.html',{'listings':rooms})