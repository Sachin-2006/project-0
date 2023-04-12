from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	uploader = models.ForeignKey(User,on_delete = models.CASCADE)
	image = models.ImageField(null = True,blank=True)
	description = models.TextField()



#class Comments(models.Model):
	
		
