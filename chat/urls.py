from django.urls import path
from .views import *

urlpatterns = [

path("chat/<str:user>",chat_box,name="chatbox")

]