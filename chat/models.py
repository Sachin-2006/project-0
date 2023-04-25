from django.db import models
from core.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save


class ChatModel(models.Model):
	c_user = models.ForeignKey(User,on_delete=models.CASCADE,default=0)
	chat_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="chat_user",default=1)

	def save(self,*args,**kwargs):
		c_user = self.c_user
		chat_user = self.chat_user
		if c_user == chat_user:
			raise ValidationError
		else:
			super(ChatModel, self).save(*args, **kwargs)




class Message(models.Model):
	cm = models.ForeignKey(ChatModel,on_delete=models.CASCADE)
	data = models.CharField(max_length=100000)
	date = models.DateTimeField(auto_now_add=True)
	
