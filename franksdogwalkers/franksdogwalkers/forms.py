from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from user.models import Profile
from phonenumber_field.modelfields import PhoneNumberField



class UserForm(forms.ModelForm): 
	walker = forms.BooleanField(required=False)
	class Meta: 
		model = User
		fields = ('username', 'password', 'first_name', 'last_name', 'email')

	# if walker is checked, then add to walker group / create walker instance 


class ProfileForm(forms.ModelForm): 

	class Meta: 
		model = Profile
		fields = ('phone',) 