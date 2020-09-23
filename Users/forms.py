from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


#DAY_CHOICES = [('1','1'),
#			('2','2'),('3','3')]
#MONTH_CHOICES = [('January','JANUARY'),('Febuary','FEBUARY')]
#YEAR_CHOICES = [('1999','1999'),('2000','2000'),('2001','2001')]
class UserRegisterForm(UserCreationForm):
	
	#email = forms.EmailField()
	#day	  = forms.IntegerField(widget=forms.Select(choices=DAY_CHOICES),)
	#month = forms.CharField(widget=forms.Select(choices=MONTH_CHOICES),)
	#year  = forms.IntegerField(widget=forms.Select(choices=YEAR_CHOICES),)
	

	class Meta:
		model = User
		fields = ['username','password1','password2']

