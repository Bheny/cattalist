from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.core.mail import EmailMessage 
from django.http import  JsonResponse
# Create your views here.

def register(request):
	if request.method == 'POST':
		data= request.POST
		print(data)
		form = UserRegisterForm(data)
		if form.is_valid():
			new_user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('login')
		else:
			messages.success(request, f'Error creating Account !!')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})	
'''

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm2(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Account created!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})	
'''

def validate_username(request):
	username = request.GET.get('username', None)
	print(username)
	value = 2
	data = {
		'is_taken': User.objects.filter(username__iexact=username).exists(),
		'others':value,

	}
	print(data)
	return JsonResponse(data, safe=False)

def activate(request, uidb64, token):
	User = get_user_model()
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
		if user is not None and account_activation_token.check_token(user, token):
			user.is_active = True
			user.save()
			login(request, User)
			return HttpResponse('Thank you for your confirmation .. now login ')
		else:
			return HttpResponse('Activation link is invalid')


