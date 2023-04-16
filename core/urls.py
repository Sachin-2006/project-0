from django.urls import path
from .views import *
#{% url 'follow' prof.username %}
urlpatterns = [

path('',home,name ="home"),
path("profile/<str:username>",show_profile,name="show_profile"),
path("follow/<str:username>",follow_unfollow,name="follow"),
path("update_profile",update_profile,name="update_profile")

]