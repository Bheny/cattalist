from .models import Profile
from django.contrib.auth.models import User 
def wishlist(request):
	items = []
	if request.user.is_authenticated:
		current_user = request.user.id
		user = User.objects.get(id=current_user)
		favorites = user.profile.wishlist.values_list()
		items = []
		for item in favorites:
			items.append(item[0])

		print(items)
	return {'wishlist':items,}