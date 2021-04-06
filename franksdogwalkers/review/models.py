from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User
from dog.models import Dog
from walker.models import Walker

# Create your models here.
class DogReview(models.Model): 
	dog_owner = models.ForeignKey(User, on_delete = models.CASCADE),
	dog = models.ForeignKey(Dog, on_delete = models.CASCADE, related_name="+")
	reviewer = models.ForeignKey(User, on_delete = models.CASCADE, related_name="+")

	score = models.IntegerField(default = 5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	message = models.TextField()
	date = models.DateTimeField(auto_now=True)


class WalkerReview(models.Model): 
	walker = models.ForeignKey(User, on_delete = models.CASCADE)
	reviewer = models.ForeignKey(User, on_delete = models.CASCADE, related_name="+")

	score = models.IntegerField(default = 5, validators=[MinValueValidator(0), MaxValueValidator(10)])
	message = models.TextField()
	date = models.DateTimeField(auto_now=True)
