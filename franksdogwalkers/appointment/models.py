from django.db import models
from django.contrib.auth.models import User

from walker.models import Walker
from dog.models import Dog

# Create your models here.
class Appointment(models.Model): 
	walker = models.ForeignKey(Walker, on_delete = models.CASCADE)
	dog1 = models.ForeignKey(Dog, on_delete=models.SET_NULL, null=True, related_name = "+")
	dog2 = models.ForeignKey(Dog, on_delete=models.SET_NULL, null=True, related_name = "+")
	dog3 = models.ForeignKey(Dog, on_delete=models.SET_NULL, null=True, related_name = "+")
	dog4 = models.ForeignKey(Dog, on_delete=models.SET_NULL, null=True, related_name = "+")
	dog5 = models.ForeignKey(Dog, on_delete=models.SET_NULL, null=True, related_name = "+")

	startime = models.TimeField()
	startloc = models.TextField()