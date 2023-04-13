from django.urls import path
from .views import *
urlpatterns = [
	
	path("addpost/",add_post,name="add_post"),
	path("comment/<int:pk>",post_comment,name="post_comment")
]