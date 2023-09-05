from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import User
from .forms import UserUpdate
from post.models import Post


def home(request):
	if request.user.is_authenticated:
		current_user = request.user
	all_posts = Post.objects.all()
	all_users = User.objects.all()
	context = {"user":request.user,"all_post":all_posts,"all_users":all_users}

	return render(request,"core/home.html",context)


def show_profile(request,username):
	user_profile = User.objects.get(username=username)
	context = {"prof":user_profile}
	return render(request,"core/show_profile.html",context)

def update_profile(request):
	if request.user.is_authenticated and request.method=="POST":
		current_user = User.objects.get(id=request.user.id)
		form = UserUpdate(request.POST,request.FILES,instance=current_user)
		
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			form = UserUpdate(instance=current_user)
			return render(request,"core/update_user.html",{"form":form})
	return redirect(request,"not authen")



#following and unfollowing users

def follow_unfollow(request,username):
	user = User.objects.get(username=username)
	current_user = User.objects.get(username=request.user.username)
	following = user.following.all()

	if username != current_user.username:
		if current_user in following:
			print("follow")
			user.following.remove(current_user.id)
		else:
			
			user.following.add(current_user.id)
	return HttpResponseRedirect(reverse("show_profile",args=[user.username]))

