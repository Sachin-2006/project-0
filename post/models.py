from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
	uploader = models.ForeignKey(User,on_delete = models.CASCADE)
	image = models.ImageField(null = True,blank=True)
	description = models.TextField()



class Comment(models.Model):
	critic = models.ForeignKey(User,on_delete = models.CASCADE)
	post = models.ForeignKey(Post,on_delete = models.CASCADE)
	descr = models.TextField()
	created_date = models.DateTimeField(default=timezone.now())

	
		
