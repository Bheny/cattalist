from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from .models import Listing,Policy, Room, Event, Place, Amenity, Room_Review, Place_Review, Listing_Review, Event_Review

from profiles.models import Profile, Host_Review

def room_detail(request, id, slug):
	room = get_object_or_404(Room,
							 id=id,
							 slug=slug,
							 available=True)

	reviews = Room_Review.objects.filter(item=room)
	comments = Host_Review.objects.filter(item=room.structure.owner.profile)
	rules = Policy.objects.filter(title="House Rules")
	safety = Policy.objects.filter(title="Safety")
	Moving = Policy.objects.filter(title="Moving")
	
	context = {'room':room,'reviews':reviews,
			   'comments':comments,'rules':rules,
			   'Safety':safety}
	return render(request, 'details.html', context)