from django.shortcuts import render
from .services import search, list_all
# Create your views here.
def home(request,result=False ):
	if request.method == 'POST':
		context = search(request.POST)
	else:
		context = list_all()
	return render(request, 'index.html',context)



def about(request):
	return render(request, 'about.html', {})

def landing(request):
	return render(request, 'landing.html', {})

