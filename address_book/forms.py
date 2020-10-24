from django import forms
from .models import address

class addressform(forms.ModelForm):
	class Meta:
		model = address
		fields = ["name" , "email" , "phone" , "address" , "city" , "state" , "zipcode"]