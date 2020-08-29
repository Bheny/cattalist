from django.db import models

# Create your models here.
class MyUser(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=32)

	def __str__(self):
		return self.id


