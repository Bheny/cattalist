from listing.models import Listing, Room, Place
from location.models import Area
from profiles.models import Search_History

def retrieve(Type, location):

	rooms = Room.objects.all()
	locations = Area.objects.all()

	#Type = data['type']
	#location = data['location']
	
	if Type == "all" and location != "all":
		rooms = Room.objects.filter(location=location)
		result = True

	elif Type != "all" and location == "all":
		rooms = Room.objects.filter(max_quantity=Type)
		result = True

	elif location == "all" or Type == "all":
		rooms = Room.objects.all()[:10]
		result = True
		

	else:
		rooms = Room.objects.filter(location=location).filter(max_quantity=Type)
		result = True
	
	return {'listings':rooms,'results':result,'areas':locations}


def list_all():
	rooms = Room.objects.all().order_by('-created')[:4]
	locations = Area.objects.all()
	places = Place.objects.all()
	return {'listings':rooms,'areas':locations, 'places':places	}