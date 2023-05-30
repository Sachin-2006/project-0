from django.shortcuts import render,redirect
from .models import *
from core.models import User
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import MessageSerializer,UserSerializer
from .models import Message
from django.utils.safestring import mark_safe
from urllib.parse import quote
import json

def chatPage(request,username):

	user = User.objects.get(username=username)
	if request.user.is_mutual(user):

		if user.id < request.user.id:
			username = "chat"+str(user.username)+"_"+str(request.user.username)
		else:
			username = "chat"+str(request.user.username)+"_"+str(user.username)
		user_chat_name = mark_safe(quote(username))
		messages = Message.objects.filter(room_name=user_chat_name)
		lst =[]
		user1 = request.user
		followers = user1.followers.all()
		for i in followers:
			print(i)
			u = User.objects.get(username=i)
			if u.is_mutual(user1):
				lst.append(u)
		context = {'room_name_json' : mark_safe(json.dumps(str(user_chat_name))),
		"receiver":str(user),
		"messages":messages,
		"follow":lst,
		}
	else:
		return redirect('/')
	return render(request, "chat/chatbox.html", context)

