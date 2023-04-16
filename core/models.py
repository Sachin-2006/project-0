from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.db.models.signals import post_save
	

class User(AbstractUser):
	following = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical=False)
	profile_pic = models.ImageField(upload_to="profile_pics", default="profile_pics/default_profile_pic.jpg")
	bio = models.TextField(default="Hello!")

