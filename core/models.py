from django.db import models
from django.contrib.auth.models import AbstractUser 


class User(AbstractUser):
	following = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical=False)
	profile_pic = models.ImageField(upload_to="profile_pics", default="profile_pics/default_profile_pic.jpg")
	bio = models.TextField(default="Hello!")

	def is_mutual(self,another_user):
		return self in another_user.following.all() and another_user in self.following.all()
		