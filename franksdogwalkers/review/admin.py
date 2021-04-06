from django.contrib import admin
from .models import DogReview, WalkerReview

# Register your models here.
admin.site.register(DogReview)
admin.site.register(WalkerReview)