from listing.models import Listing, Room
from location.models import Area

def search(data):
	rooms = Room.objects.all()
	locations = Area.objects.all()

	Type = data['type']
	location = data['location']
	
	if Type == "all" and location != "all":
		rooms = Room.objects.filter(location=location)
		result = True
	elif Type != "all" and location == "all":
		rooms = Room.objects.filter(max_quantity=Type)
		result = True

	elif location == "all" or Type == "all":
		rooms = Room.objects.all()[:10]
		result = True
		print(result)

	else:
		rooms = Room.objects.filter(location=location).filter(max_quantity=Type)
		result = True
	
	return {'listings':rooms,'results':result,'areas':locations}


def list_all():
	rooms = Room.objects.all()
	locations = Area.objects.all()
	return {'listings':rooms,'areas':locations}