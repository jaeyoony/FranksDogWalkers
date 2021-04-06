from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# walker model that extends the users model
class Walker(models.Model): 
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	rating = models.FloatField(default = 0.0, blank = True)
	available = models.BooleanField(default = False)

	def get_absolute_url(self): 
		return reverse("user:user_profile", kwargs={"id": self.user.id})