from django.shortcuts import render
from django.views import View
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
class AppointmentListView(View): 
	template_name = "appointment_list.html"
	# get only the appointments with your name in it
	queryset = Appointment.objects.filter()
	context = {}

	def get(self, request, *args, **kwargs): 
		if request.user.is_authenticated: 
			apptlist = Appointment.objects.filter(creator__pk = request.user.id)
			self.context['appointments'] = apptlist
			return render(request, self.template_name, self.context)
		else: 
			return redirect('login')


# get details on a single appointmentv
class AppointmentDetailView(DetailView): 
	template_name = "appointmnet_detail.html"
	queryset = Appointment.objects.all()

# creates an appointment
class AppointmentCreateView(View): 
	template_name = "appointment_create.html"
	queryset = Appointment.objects.all()
	context = {}

	def get(self, request, *args, **kwargs): 
		if request.user.is_authenticated: 
			self.context.clear()
			self.context['form'] = AppointmentForm
			return render(request, self.template_name, self.context)
		else: 
			return redirect('login')

	def post(self, request, *args, **kwargs): 
		form = AppointmentForm(request.POST)
		if form.is_valid(): 
			new_appt = form.save(commit=False)
			new_appt.creator = request.user
			new_appt.save()
			return redirect("appointments:appointment_list")
		else: 
			self.context['form'] = AppointmentForm()
			self.context['error'] = "Appointment not made"
			return render(request, self.template_name, self.context)