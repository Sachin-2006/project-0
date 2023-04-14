from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)



class Post(models.Model):
	uploader = models.ForeignKey(User,on_delete = models.CASCADE)
	image = models.ImageField(null = True,blank=True,upload_to = "")
	description = models.TextField()
	likes = models.ManyToManyField(User,related_name="post_like")

	def total_like(self):
		return self.likes.count()




class Comment(models.Model):
	critic = models.ForeignKey(User,on_delete = models.CASCADE)
	post = models.ForeignKey(Post,related_name = "comments",on_delete = models.CASCADE)
	descr = models.TextField()
	created_date = models.DateTimeField(auto_now_add = True)


		

