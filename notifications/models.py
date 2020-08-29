from django.db import models
from profiles.models import Profile
# Create your models here.
class Notification(models.Model):
	sender = models.ForeignKey(Profile, related_name="sender", on_delete=models.CASCADE)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)