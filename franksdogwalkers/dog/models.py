from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Dog(models.Model): 
	firstname = models.CharField(max_length = 32)
	lastname = models.CharField(max_length = 32, blank = True)
	breed = models.CharField(max_length = 32, blank = True)
	size = models.CharField(max_length = 10, choices= [
		('S', 'Small'), 
		('M', 'Medium'), 
		('L', 'Large')
	])
	owner = models.ForeignKey(User, on_delete= models.CASCADE)
	rating = models.FloatField(default = 0.0, blank = True)

	def get_absolute_url(self): 
		return reverse("dog:dog_detail", kwargs={"id": self.id})