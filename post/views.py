from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import AddPost,AddComment


def add_post(request):
	if request.method == "POST" and request.user.is_authenticated:
		f = AddPost(request.POST)
		form = f.save(commit=False)
		form.uploader = request.user
		form.save()
		return redirect('/')
	f = AddPost()
	context = {"form":f}
	return render(request,'post/add_post.html',context)

def post_comment(request,pk):
	current_post = get_object_or_404(Post,id=id)
	if request.method =="POST" and request.user.is_authenticated:
		f = AddComment(request.POST)
		form = f.save(commit = False)
		form.critic = request.user

		form.post = current_post
		form.save()
		return redirect('/')
	f = AddComment()
	context = {"form":f,"post":current_post}
	return render(request,"post/comment_post.html",context)

