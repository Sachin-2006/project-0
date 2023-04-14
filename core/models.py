from django.db import models
from django.contrib.auth.models import User


class ProfileDetail(models.Model):
	profile = models.ForeignKey(User,on_delete = models.CASCADE,related_name="profile_deltails")
	profile_pic = models.ImageField(upload_to="profile_pics")
	bio = models.TextField()
	
