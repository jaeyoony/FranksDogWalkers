from django.urls import path
from .views import (
	WalkerReviewListView, 
	WalkerReviewDetailView,  
	DogReviewListView, 
	DogReviewDetailView,
)

app_name = "review"
urlpatterns = [
	path('walkers/', WalkerReviewListView.as_view(), name="walker_rev_list"), 
	path('walkers/<int:id>', WalkerReviewListView.as_view(), name="given_walker_rev_list"),
	path('walkers/get/<int:id>', WalkerReviewDetailView.as_view(), name="walker_rev_detail"),

	path('dogs/', DogReviewListView.as_view(), name="dog_rev_list"),
	path('dogs/<int:id>', DogReviewListView.as_view(), name="given_dog_rev_list"),
	path('dogs/get/<int:id>', DogReviewDetailView.as_view(), name="dog_rev_detail"),
]