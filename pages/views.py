from django.shortcuts import render
from .services import retrieve, list_all
from services.models import Request
# Create your views here.

def home(request ):
	
	context = list_all()
	return render(request, 'index.html',context)

def lookup(request):
	context = {}
	print(request)
	data = request.POST
	
	if data:
		context = retrieve(data['type'],data['location'])
		print(context)
	return render(request, 'results.html',context)

def booking_requests(request):
	requests = Request.objects.filter(owner=request.user)
	return render(request, 'requests.html',{'requests':requests})

def about(request):
	return render(request, 'about.html', {})

def landing(request):
	return render(request, 'landing.html', {})

