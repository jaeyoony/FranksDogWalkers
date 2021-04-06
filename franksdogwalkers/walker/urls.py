from django.urls import path
from .views import (
	WalkerListView, 
	WalkerDetailView
)

app_name = 'walkers'
urlpatterns = [
	path('', WalkerListView.as_view(), name="walker_list"),
	path('<int:id>/', WalkerDetailView.as_view(), name="walker_page"),
]