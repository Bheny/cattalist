from django import forms 
from .models import Policy, Room, Listing


class ListingAdminForm(forms.ModelForm):
	TYPES = [
		('GH', 'Guest House'),
		('RTA', 'Rental Apartment'),
		('HTL', 'Hotel'),
		('SHP','Shop'),
		('PRK', 'Park'),
		('CSR', 'Class room'),
		('CRH', 'Church'),
	]

	Type = forms.CharField(widget=forms.Select(choices=TYPES),)

	class Meta:
		model = Listing
		fields = ['image','name','slug','Type','description','location','available','owner','digital_address','star_1','star_2','star_3','star_4','star_5']

class PolicyAdminForm(forms.ModelForm):
	OPTIONS = [
	('HOUSE RULES','house rules'),
	('SAFETY & PROPERTY','safety & property'),
	('MOVING POLICY','moving policy'),
	]
	title = forms.CharField(widget=forms.Select(choices=OPTIONS),)

	class Meta:
		model = Policy 
		fields = ['title','content']

class RoomAdminForm(forms.ModelForm):
	RATES = [
	('Yr','Yr'),
	('Mon','Mon'),
	('Sem','Sem'),
	('Night','night')
	]

	OPTIONS = (
			("TLT", "Toilet"),
			("BTH", "Bath"),
			("KTN", "Kitchen"),
			("PLR", "Palour"),
		)
	rate = forms.CharField(widget=forms.Select(choices=RATES),)
	utilities = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS)

	class Meta:
		model = Room
		#fields = ['image','name','slug','description','area','town','region','available','places','owner','amenities','digital_address',]
		fields = ['structure','image','name','slug','available','price','description','location','max_quantity','rate','utilities']



	