from django.shortcuts import render,redirect
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
	if request.method =="POST" and request.user.is_authenticated:
		f = AddComment(request.POST)
		form = f.save(commit = False)
		form.critic = request.user
		current_post = Post.objects.get(pk=pk)
		if current_post is not None:
			form.post = current_post
			form.save()
			return redirect('/')
		else:
			return render(request,'404.html')
	f = AddComment()

	context = {"form":f}
	return render(request,"post/comment_post.html",context)

