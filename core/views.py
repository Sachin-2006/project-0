from django.shortcuts import render
from post.models import Post


def home(request):
	if request.user.is_authenticated:
		current_user = request.user
	all_posts = Post.objects.all()
	context = {"user":request.user,"post":all_posts}
	return render(request,"core/home.html",context)

