from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404

from django.views.generic import(
	ListView, 
	DetailView
)

from .models import Profile

# Create your views here.

# list of all users
class UserListView(ListView): 
	template_name = "profile_list.html"
	queryset = Profile.objects.all()

# view for user detail page
class UserDetailView(DetailView): 
	template_name = "profile_page.html"
	queryset = User.objects.all()

	def get_object(self): 
		id_ = self.kwargs.get("id")
		try: 
			user = User.objects.get(pk=id_)
		except User.DoesNotExist: 
			raise Http404("User does not exist")
		return user.profile


# # view for user creation
# class SignupView(View): 

	# every time a user is created, make sure to also create that User's profile