from django.contrib import admin
from .models import Listing, Amenity, Event, Policy,\
					 Room, Place, Room_Review, Place_Review, Listing_Review, Event_Review
from .forms import PolicyAdminForm, RoomAdminForm

class ListingAdmin(admin.ModelAdmin):
	
	#fields = ['image','name','slug']
	# sets up slug to be generated from product name
	prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Listing,ListingAdmin)


admin.site.register(Amenity)

class RoomAdmin(admin.ModelAdmin):
	form = RoomAdminForm
	
	prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Room, RoomAdmin)

class PlaceAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Place, PlaceAdmin)

admin.site.register(Event)

admin.site.register(Room_Review)
admin.site.register(Listing_Review)
admin.site.register(Place_Review)
admin.site.register(Event_Review)

class PolicyAdmin(admin.ModelAdmin):
	form = PolicyAdminForm
	fields = ['title','content']

admin.site.register(Policy, PolicyAdmin)