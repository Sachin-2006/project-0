from django.db import models
from django.contrib.auth.models import User


class ProfileDetail(models.Model):
	profile = models.ForeignKey(User,on_delete = models.CASCADE,related_name="profile_deltails")
	profile_pic = models.ImageField(upload_to="profile_pics")
	bio = models.TextField()
	
class Follower(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	another_user = models.ManyToManyField(User,related_name="another_user")
	