from django.urls import path
from .views import (
	DogListView, 
	DogAddView, 
	DogDetailView
)

app_name = 'dog'
urlpatterns = [
	path('', DogListView.as_view(), name="dog_list"),
	path('add', DogAddView.as_view(), name="dog_add"),
	path('<int:id>', DogDetailView.as_view(), name="dog_detail"),
]