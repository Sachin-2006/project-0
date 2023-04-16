from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class ProfileDetail(models.Model):
	profile = models.ForeignKey(User,on_delete = models.CASCADE,related_name="profile_deltails")
	profile_pic = models.ImageField(upload_to="profile_pics", default="profile_pics/default_profile_pic.jpg")
	bio = models.TextField(default="Hello!")




class Follower(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	another_user = models.ManyToManyField(User,related_name="a_user",blank=True)





def create_follower(sender,instance,created,**kwargs):
	if created:
		user_follow = Follower(user=instance)
		user_follow.save()


post_save.connect(create_follower,sender=User)


def create_profile(sender,instance,created,**kwargs):
	if created:
		user_profile = ProfileDetail(profile=instance)
		user_profile.save()

post_save.connect(create_profile,sender=User)