from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.http import Http404

from django.views.generic import(
	ListView, 
	DetailView
)

from .models import Walker

# Create your views here.
class WalkerListView(ListView): 
	template_name = "walker_list.html"
	queryset = User.objects.filter(groups__name="Walkers")

class WalkerDetailView(DetailView): 
	template_name = "walker_page.html"
	queryset = User.objects.filter(groups__name="Walkers")

	def get_object(self): 
		id_ = self.kwargs.get("id")
		try: 
			user = User.objects.get(pk=id_)
		except user.DoesNotExist: 
			raise Http404("Walker does not exist")
		return user