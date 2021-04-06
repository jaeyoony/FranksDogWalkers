from django.shortcuts import render
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView
)
from .models import Appointment 
from .forms import AppointmentForm

# Create your views here.

# get list of all appointments
# should only get appointments relevant to the user
class AppointmentListView(ListView): 
	template_name = "appointment_list.html"
	# get only the appointments with your name in it
	queryset = Appointment.objects.all()

# get details on a single appointmentv
class AppointmentDetailView(DetailView): 
	template_name = "appointmnet_detail.html"
	queryset = Appointment.objects.all()

# creates an appointment
class AppointmentCreateView(CreateView): 
	template_name = "appointment_create.html"
	queryset = Appointment.objects.all()
	form_class = AppointmentForm