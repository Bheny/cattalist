from django import forms 
from .models import Policy, Room

OPTIONS = [
	('HOUSE RULES','house rules'),
	('SAFETY & PROPERTY','safety & property'),
	('MOVING POLICY','moving policy'),
]

RATES = [
	('Yr','Yr'),
	('Mon','Mon'),
	('Sem','Sem'),
]

class PolicyAdminForm(forms.ModelForm):
	title = forms.CharField(widget=forms.Select(choices=OPTIONS),)

	class Meta:
		model = Policy 
		fields = ['title','content']

class RoomAdminForm(forms.ModelForm):
	rate = forms.CharField(widget=forms.Select(choices=RATES),)

	class Meta:
		model = Room
		#fields = ['image','name','slug','description','area','town','region','available','places','owner','amenities','digital_address',]
		fields = ['structure','image','name','slug','available','price','description','location','max_quantity','rate',]