from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
	class Meta:
		model = Travel
		fields = '__all__'