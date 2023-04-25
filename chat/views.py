from django.shortcuts import render,redirect
from .models import *
from core.models import User


def chat_box(request,user):
	user = User.objects.get(username=user)
	if user is not None:	
		if request.user.is_mutual(user):
			cm = ChatModel(c_user=request.user,chat_user=user)	
			cm.save()
			print("nope")
		return redirect('show_profile',username=user)
	else:
		return redirect('chatbox',user=user)

	context = {"user":user}
	return redirect('/')
def messaging(request,user):
	