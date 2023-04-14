from django.shortcuts import render,get_object_or_404
from post.models import Post
from .models import ProfileDetail
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



