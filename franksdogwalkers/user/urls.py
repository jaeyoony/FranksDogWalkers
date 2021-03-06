from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
	UserListView,
	UserDetailView, 
)

app_name = 'user'
urlpatterns = [
	path('', UserListView.as_view(), name='user_list'),
	path("<int:id>/", UserDetailView.as_view(), name='user_profile'),
]