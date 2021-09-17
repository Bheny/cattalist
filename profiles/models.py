from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from listing.models import Room

# collects products liked by the owner of this profile


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default/profile.jpg', upload_to='profile_pics')
	#favorites = models.ForeignKey(Favorites, related_name="favs", on_delete=models.CASCADE, blank=True, null=True)
	watchlist = models.ManyToManyField(Room, related_name="wishlist" ,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.user.username} Profile'  


class Host_Review(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Profile, related_name="review", on_delete=models.CASCADE)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Search_History(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	keyword = models.CharField(max_length=600)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return u'%s by %s' %(self.keyword,self.user)
    