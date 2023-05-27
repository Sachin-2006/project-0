from django.urls import path
from .views import *

urlpatterns = [
path("chat/<str:username>", chatPage, name="chat-page"),
path("chatlist/<str:username>",chatlist,name="chat-list"),
]
 
