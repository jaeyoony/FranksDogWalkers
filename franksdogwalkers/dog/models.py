from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dog(models.Model): 
	firstname = models.CharField(max_length = 32)
	lastname = models.CharField(max_length = 32, blank = True)
	owner = models.ForeignKey(User, on_delete= models.CASCADE)
	rating = models.FloatField(default = 0.0, blank = True)