from django.forms import ModelForm
from .models import *

class AddPost(ModelForm):
	class Meta:
		model = Post
		fields = ["image","description"]

class AddComment(ModelForm):
	class Meta:
		model = Comment
		fields = ["descr"]

class UpdatePost(ModelForm):
	class Meta: 
		model = Post
		fields = ["image",
		"description",

		]