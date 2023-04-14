from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from post.models import Post
from .models import ProfileDetail,Follower
from django.contrib.auth.models import User

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
	context = {"prof":user_profile}
	return render(request,"core/show_profile.html",context)


def follow_unfollow(request,pk):
	if request.method == "POST" and request.user.is_authenticated :
		current_user = request.user
		prof_user = get_object_or_404(User,id=pk)
		check_follow = get_object_or_404(Follower,user=current_user)
		
		if prof_user in check_follow.another_user :
			check_follow.objects.remove(prof_user)
		else:
			check_follow.objects.add(prof_user)
	
	return HttpResponseRedirect(reverse("show_profile"))




