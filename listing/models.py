from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from location.models import Area

class Place(models.Model):
	# This model allows us to create multiple instances of places of interest to users of the platform
	image = models.ImageField(default='home.jpg', upload_to='places/%Y/%m/%d', blank=True)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, help_text='Unique value for place page URL, created from name.')
	kind = models.CharField(max_length=255)
	
	available = models.BooleanField()
	location = 	models.CharField(max_length=255)
	digital_address = models.CharField(max_length=50, blank=True)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	count = models.PositiveIntegerField(default=0, blank=True)

	'''
	def total_rating(self):
			from .models import Place
			review = Place.objects.get(id=self.id)
			rating = (1*review.star_1 + 2*review.star_2 + 3*review.star_3 + 4*review.star_4 + 5*review.star_5)  
			sum_n  = (review.star_1 + review.star_2 +review.star_3+ review.star_4 +review.star_5 )
			total = 0
			if sum_n != 0:
				total = rating / sum_n
			return round(total,1)
	'''

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		#return f"/category/{self.slug}/"
		return reverse('listings:places_list', args=[self.slug])

class Place_Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Place, related_name="review", on_delete=models.CASCADE)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user.username


class Listing(models.Model):
	image = models.ImageField(default='home.jpg', upload_to='listings/%Y/%m/%d', blank=True)
	name  = models.CharField(max_length=255)
	slug  = models.SlugField(max_length=255, unique=True, db_index=True,
											help_text='Unique value for product page URL, created from name.')
	description = models.TextField(blank=True)
	type = models.CharField(max_length=255,default="hostel")
	price = models.DecimalField(default=0,max_digits=999, decimal_places=2)
	location = models.ForeignKey(Area, related_name="listing_area", on_delete=models.DO_NOTHING)
	available = models.BooleanField()
	owner = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
	#amenities = models.ManyToManyField(Amenity, related_name='Amenities')
	digital_address = models.CharField(max_length=50, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	count = models.PositiveIntegerField(default=0, blank=True)
	
	'''
	def total_rating(self):
			from .models import Listing
			review = Listing.objects.get(id=self.id)

			rating = (1*review.star_1 + 2*review.star_2 + 3*review.star_3 + 4*review.star_4 + 5*review.star_5)  
			sum_n  = (review.star_1 + review.star_2 +review.star_3+ review.star_4 +review.star_5 )
			total = 0
			if sum_n != 0:
				total = rating / sum_n
			return round(total,1)
	'''
	def __str__(self):
		return self.name
	

class Listing_Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Listing, related_name="review", on_delete=models.CASCADE)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username


class Policy(models.Model):
	title = models.CharField(max_length=255)
	content = models.CharField(max_length=255)

	def __str__(self):
		return self.title

#======================================= Room Model ===========================
class Room(models.Model):
	structure = models.ForeignKey(Listing, related_name="structure", on_delete=models.CASCADE)
	image = models.ImageField(default='home.jpg', upload_to='listings/rooms/%Y/%m/%d', blank=True)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, help_text='Unique value for room page URL, created from name.')
	available = models.BooleanField()
	price = models.PositiveIntegerField(default=0)
	rate = models.CharField(max_length=255,default="Mon")
	description = models.TextField(blank=True)
	location = models.ForeignKey(Area, related_name="room_area", on_delete=models.DO_NOTHING)
	max_quantity = models.PositiveIntegerField(default=1)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	count = models.PositiveIntegerField(default=0, blank=True)
	star_1 = models.PositiveIntegerField(default=0, blank=True)
	star_2 = models.PositiveIntegerField(default=0, blank=True)
	star_3 = models.PositiveIntegerField(default=0, blank=True)
	star_4 = models.PositiveIntegerField(default=0, blank=True)
	star_5 = models.PositiveIntegerField(default=0, blank=True)

	def total_rating(self):
			from .models import Listing
			review = Listing.objects.get(id=self.id)

			rating = (1*review.star_1 + 2*review.star_2 + 3*review.star_3 + 4*review.star_4 + 5*review.star_5)  
			sum_n  = (review.star_1 + review.star_2 +review.star_3+ review.star_4 +review.star_5 )
			total = 0
			if sum_n != 0:
				total = rating / sum_n
			return round(total,1)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return f"/category/{self.slug}/"
		return reverse('listing:room_detail', args=[self.id,self.slug])

class Room_Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Room, related_name="review", on_delete=models.CASCADE)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username


class Event(models.Model):
	# here intances of events can be created 
	image = models.ImageField(default='home.jpg', upload_to='events/%Y/%m/%d', blank=True)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, help_text='Unique value for event page URL, created from name.')
	available = models.BooleanField()
	description = models.TextField(blank=True)
	start = models.DateTimeField()
	end = models.DateTimeField()
	location = models.ForeignKey(Area, related_name="event_area", on_delete=models.DO_NOTHING)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	count = models.PositiveIntegerField(default=0, blank=True)
	star_1 = models.PositiveIntegerField(default=0, blank=True)
	star_2 = models.PositiveIntegerField(default=0, blank=True)
	star_3 = models.PositiveIntegerField(default=0, blank=True)
	star_4 = models.PositiveIntegerField(default=0, blank=True)
	star_5 = models.PositiveIntegerField(default=0, blank=True)

	def total_rating(self):
			from .models import Event
			review = Event.objects.get(id=self.id)

			rating = (1*review.star_1 + 2*review.star_2 + 3*review.star_3 + 4*review.star_4 + 5*review.star_5)  
			sum_n  = (review.star_1 + review.star_2 +review.star_3+ review.star_4 +review.star_5 )
			total = 0
			if sum_n != 0:
				total = rating / sum_n
			return round(total,1)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return f"/category/{self.slug}/"
		return reverse('listings:event_list', args=[self.slug])

class Event_Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Event, related_name="review", on_delete=models.CASCADE)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user.username




class Amenity(models.Model):
	structure = models.ForeignKey(Listing, related_name="structure_amenity", on_delete=models.CASCADE, blank="True")
	room = models.ForeignKey(Room, related_name="room_amenity", on_delete=models.CASCADE, blank=True)
	image = models.ImageField(default='home.jpg', upload_to='amenities/%Y/%m/%d', blank=True)
	name = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name