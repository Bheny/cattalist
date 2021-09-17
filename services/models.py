from django.db import models
from django.contrib.auth.models import User 
from listing.models import Room
# Create your models here.

class Booking(models.Model):
	user =  models.ForeignKey(User, related_name="customers", on_delete=models.CASCADE)
	place = models.ForeignKey(Room, related_name="room", on_delete=models.CASCADE)
	check_in = models.DateTimeField()
	check_out = models.DateTimeField()
	quantity = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return u' %s booked by %s' % (self.place.name,self.user.username)



class Request(models.Model):
	owner = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
	customer =  models.ForeignKey(User, related_name="requesting_customer", on_delete=models.CASCADE)
	place = models.ForeignKey(Room, related_name="requested_room", on_delete=models.CASCADE)
	sent = models.BooleanField(default=False)
	accepted = models.BooleanField(default=False)
	seen = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return u' %s requested by %s' % (self.place.name,self.customer.username)
