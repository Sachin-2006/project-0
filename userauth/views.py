from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout,authenticate
from django.contrib import messages
from django.contrib.auth import login as authlogin
from django.contrib.auth.forms import AuthenticationForm
from core.models import Follower 
from .forms import *


def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			authlogin(request,user)
			messages.success(request,"super adipoli")
			return redirect("/")
		messages.error(request,"Sry da thabi thappu irruku")
	form = UserForm()
	context = {"form":form}
	return render(request,"userauth/signup.html",context)


def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get("password")
			user = authenticate(username=username,password = password)
			if user is not None:
				authlogin(request,user)
				messages.success(request,"Ok!!")
				return redirect("/")
			else:
				messages.error(request,"ERROR!!!!")
	form = AuthenticationForm()
	context = {"login_form":form}
	return render(request,"userauth/signin.html",context)


def logout_view(request):
	logout(request)
	return redirect("/")




