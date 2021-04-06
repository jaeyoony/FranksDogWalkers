from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, ProfileForm
from django.views.generic import(
	UpdateView
)


# view for the landing/home page
class HomepageView(View): 
	template_name = "homepage.html"

	def get(self, request, *args, **kwargs): 
		return render(request, self.template_name, {})

# singup view class
class Signupview(View): 
	template_name = "signup.html"
	context = {}

	def get(self, request, *args, **kwargs): 
		self.context.clear()
		self.context['user_form'] = UserCreationForm()
		return render(request, self.template_name, self.context)

	# post request - check for valid user creation
	def post(self, request, *args, **kwargs): 
		# create a filled instance of the createform using http request
		userform = UserCreationForm(request.POST)

		if userform.is_valid(): 
			# save user
			userform.save()

			username = userform.cleaned_data.get('username')
			pw = userform.cleaned_data.get('password1')
			user = authenticate(username = username, password = pw)
			login(request, user)

			# send logged in user to homepage
			return redirect("homepage")

		else: 
			self.context['user_form'] = UserCreationForm()
			self.context['error'] = "something went wrong with creating user"
			return render(request, self.template_name, self.context)

