from django.urls import path
from .views import (
	AppointmentListView, 
	AppointmentDetailView, 
	AppointmentCreateView,
)


app_name = "appointments"

urlpatterns = [
	path('', AppointmentListView.as_view(), name="appointment_list"), 
	path('add', AppointmentCreateView.as_view(), name="appointment_add")
]
