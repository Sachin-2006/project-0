from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import AddPost,AddComment,UpdatePost
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json


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
	current_post = get_object_or_404(Post,id=pk)
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

def update_post(request,pk):
	current_post = get_object_or_404(Post,id=pk)
	if request.method == "POST":
		form = UpdatePost(request.POST,request.FILES,instance=current_post)
		if form.is_valid():
			form.save()

	else:
		form = UpdatePost(instance=current_post)
	context = {"form":form}
	return render(request,"post/update_post.html",context)

@csrf_exempt
def post_like(request):
	is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
	print(1)
	if request.method == "POST":
		print(2)
		if is_ajax:
			print(3)
			post = get_object_or_404(Post,pk=request.POST.get("content_id",None))
			
			print(post)
			if post.likes.filter(id=request.user.id):
				post.likes.remove(request.user)
				add = False
				print(4)
			else:
				add = True
				post.likes.add(request.user)
			print(5)
			context = {'content_id':request.POST.get("content_id",None)}
			return HttpResponse(json.dumps(context),content_type="application/json")
			
	else:
		print("nope!!")
		return HttpResponseBadRequest("invalid")



