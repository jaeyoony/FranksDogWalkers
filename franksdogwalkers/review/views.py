from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import(
	CreateView, 
	DetailView
)
from .models import DogReview, WalkerReview

# Create your views here.


# get the list of reviews about a particular walker
class WalkerReviewListView(View): 
	template_name = "rev_list.html"
	context = {}

	def get(self, request, *args, **kwargs): 
		self.context.clear()
		id_ = self.kwargs.get("id")
		self.context['rtype'] = "walkerreview"
		# if id was specified, then get specific list of reviews
		if id_: 
			self.context['reviews'] =  WalkerReview.objects.filter(walker__pk = id_)
			return render(request, self.template_name, self.context)
		# else, get all reviews
		else: 
			self.context['reviews'] = WalkerReview.objects.all()
			return render(request, self.template_name, self.context)


# get the details on a specific review on a walker
class WalkerReviewDetailView(DetailView): 
	template_name = "rev_detail.html"
	queryset = WalkerReview.objects.all()

	def get_object(self): 
		rid = self.kwargs.get('id')
		return get_object_or_404(WalkerReview, pk=rid)

# leave a review on a walkwer
# class CreateWalkerReview(View): 

# get the list of reviews on a particular dog
class DogReviewListView(View): 
	template_name = "rev_list.html"
	context = {}

	def get(self, request, *args, **kwargs): 
		self.context.clear()
		id_ = self.kwargs.get("id")
		self.context['rtype'] = 'dogreview'
		if id_:		
			self.context['reviews'] = DogReview.objects.filter(dog__pk = id_)
			return render(request, self.template_name, self.context)
		else: 
			self.context['reviews'] = DogReview.objects.all()
			return render(request, self.template_name, self.context)

# get the details on a specific review on a dog 
class DogReviewDetailView(DetailView): 
	template_name = "rev_detail.html"
	queryset = DogReview.objects.all()

	def get_object(self): 
		rid = self.kwargs.get('id')
		return get_object_or_404(DogReview, pk=rid)
		

# leave a review for a dog
# class CreateDogReview(View): 