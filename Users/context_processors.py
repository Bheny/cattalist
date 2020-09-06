from .forms import UserRegisterForm

def users(request):
	form = UserRegisterForm
	
	return {'form':form}