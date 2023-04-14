from django.urls import path
from .views import *

urlpatterns = [

path('',home,name ="home"),
path("profile/<str:username>",show_profile,name="show_profile")

]