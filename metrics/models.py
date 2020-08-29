from django.db import models
from django.contrib.auth.models import User
from listing.models import Listing , Room, Place
from profiles.models import Profile
# Create your models here.
class Review(models.Model):
	user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
	listing = models.ForeignKey(Listing, related_name="listing_rating", on_delete=models.CASCADE,blank=True)
	room = models.ForeignKey(Room, related_name="room_rating", on_delete=models.CASCADE, blank=True)
	Place = models.ForeignKey(Place, related_name="place_rating", on_delete=models.CASCADE, blank=True)
	owner = models.ForeignKey(Profile, related_name="profile_rating", on_delete=models.CASCADE, blank=True)
	message = models.TextField(blank=True)
	active = models.BooleanField(default=True)
	
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	
class Rating(models.Model):
	star_1 = models.PositiveIntegerField(default=0)
	star_2 = models.PositiveIntegerField(default=0)
	star_3 = models.PositiveIntegerField(default=0)
	star_4 = models.PositiveIntegerField(default=0)
	star_5 = models.PositiveIntegerField(default=0)

	def total_rating(self):
			from .models import Review
			review = Review.objects.get(id=self.id)

			rating = (1*review.star_1 + 2*review.star_2 + 3*review.star_3 + 4*review.star_4 + 5*review.star_5)  
			sum_n  = (review.star_1 + review.star_2 +review.star_3+ review.star_4 +review.star_5 )
			total = 0
			if sum_n != 0:
				total = rating / sum_n
			return round(total,1)