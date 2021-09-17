from django import forms
from services.models import Booking, Request


class CreateBookingForm(forms.ModelForm):

	class Meta:
		model = Booking 
		fields = [
			'user','place',
			'check_in','check_out','quantity',
			]

