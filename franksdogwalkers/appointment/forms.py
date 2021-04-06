from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm): 

	startloc = forms.CharField(label = "Starting location:", max_length = 256)
	class Meta: 
		model = Appointment
		fields = [
			'walker', 
			'dog1', 
			'dog2', 
			'dog3', 
			'dog4', 
			'dog5', 
			'startime', 
			'startloc',
		]