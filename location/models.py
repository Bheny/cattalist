from django.db import models

# Create your models here.
class Region(models.Model):
	name = models.CharField(max_length=255)
	digital_adddress = models.CharField(max_length=50, blank=True)
	decription = models.TextField(blank=True)
	active = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Town(models.Model):
	region = models.ForeignKey(Region, related_name="region", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	capital = models.BooleanField(default=False)
	digital_adddress = models.CharField(max_length=50, blank=True)
	decription = models.TextField(blank=True)
	active = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Area(models.Model):
	town = models.ForeignKey(Town, related_name="town", on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	digital_adddress = models.CharField(max_length=50, blank=True)
	decription = models.TextField(blank=True)
	active = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name