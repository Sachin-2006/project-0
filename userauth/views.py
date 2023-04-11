from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from .forms import *

def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request,"super adipoli")
			return redirect("/")
		messages.error(request,"Sry da thabi thappu irruku")
	form = UserForm()
	context = {"form":form}
	return render(request,"userauth/signup.html",context)