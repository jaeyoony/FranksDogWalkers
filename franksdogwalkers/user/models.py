from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# profile class for all users, one-to-one w/ django's Users
class Profile(models.Model): 
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	phone = PhoneNumberField()

# creates a profile every time a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): 
	if created: 
		Profile.objects.create(user=instance)


# saves profile on user save
def save_profile(sender, instance, **kwargs): 
	instance.profile.save()

	