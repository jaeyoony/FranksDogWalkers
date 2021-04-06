from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import(
	CreateView, 
	DetailView, 
)

from .models import Dog
from .forms import DogForm

# Create your views here.


# get list of yoru currently registered dogs
class DogListView(View): 
	template_name = "dog_list.html"
	context = {}

	def get(self, request, *args, **kwargs): 
		# if not logged in, send to dog_login page
		if request.user.is_authenticated: 
			doglist = Dog.objects.filter(owner__pk = request.user.id)
			self.context['dogs'] = doglist
			return render(request, self.template_name, self.context)
		else: 
			self.template_name = "dog_login.html"
			return render(request, self.template_name, {})

# Add a new dog under your name
class DogAddView(View): 
	template_name = "dog_add.html"
	queryset = Dog.objects.all()
	context = {}

	def get(self, request, *args, **kwargs): 
		if request.user.is_authenticated: 
			self.context.clear()
			self.context['form'] = DogForm()
			return render(request, self.template_name, self.context)
		else: 
			return redirect('login')

	def post(self, request, *args, **kwargs): 
		userform = DogForm(request.POST)
		if userform.is_valid(): 
			newdog = userform.save(commit=False)
			newdog.owner = request.user
			newdog.save()
			return redirect("dog:dog_list")
		else: 
			self.context['form'] = DogForm()
			self.context['error'] = "Dog not added"
			return render(request, self.template_name, self.context)

# see the details of a give dog
class DogDetailView(View): 
	template_name = "dog_detail.html"
	queryset = Dog.objects.all()
	context = {}

	def get(self, request, *args, **kwargs): 
		if request.user.is_authenticated: 
			self.context.clear()
			id_ = self.kwargs.get("id")
			doginfo = Dog.objects.get(pk = id_)
			self.context['object'] = doginfo
			return render(request, self.template_name, self.context)
		else: 
			return render(request, "dog_login.html", {})