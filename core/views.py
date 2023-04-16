from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ProfileDetail,Follower
from post.models import Post
from .forms import ProfileDetailForm

def home(request):

	if request.user.is_authenticated:
		current_user = request.user
	all_posts = Post.objects.all()
	all_users = User.objects.all()
	context = {"user":request.user,"post":all_posts,"all_users":all_users}

	return render(request,"core/home.html",context)


def show_profile(request,username):
	profile  = get_object_or_404(User,username=username)
	user_profile = get_object_or_404(ProfileDetail,profile=profile)
	context = {"prof":user_profile,"profile":profile}
	return render(request,"core/show_profile.html",context)

def update_profile(request):
	if request.user.is_authenticated and request.method=="POST":
		current_user = ProfileDetail.objects.get(id=request.user.id)
		form = ProfileDetailForm(request.POST,request.FILES ,instance=current_user)
		if form.is_valid():
			form.save()
			messages.success(request,"Success!")
			return redirect('/')
		context = {"form":form}
		return render(request,"core/update_profile.html",context)
	else:
		messages.success( request,"login First!!")
		return redirect("/")


#following and unfollowing users

def follow_unfollow(request,pk):

	if request.method == "POST" and request.user.is_authenticated :
		current_user = request.user
		prof_user = get_object_or_404(User,id=pk)
		user_profile = get_object_or_404(ProfileDetail,profile=prof_user)
		check_follow = Follower.objects.get(id=pk)
		if check_follow.another_user.exists():
			check_follow.another_user.remove(prof_user)
		else:
			check_follow.another_user.add(prof_user)
	
	return HttpResponseRedirect(reverse("show_profile",args=[user_profile]))




