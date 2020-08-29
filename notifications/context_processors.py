from .models import Notification

def notifications(request):
	print("works")
	notifications = Notification.objects.all()
	return {'notifications':notifications}