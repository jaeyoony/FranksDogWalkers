from django.urls import path
from .views import (
	UserListView,
	UserDetailView, 
)

app_name = 'users'
urlpatterns = [
	path('', UserListView.as_view(), name='user_list'),
	path("<int:id>/", UserDetailView.as_view(), name='user_profile'),
]