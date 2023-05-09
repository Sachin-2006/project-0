from django.db import models
from core.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from channels.db import database_sync_to_async

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
	sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
	room_name = models.CharField(max_length=100)
	message = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True)
	class Meta :
		ordering = ('timestamp',)

