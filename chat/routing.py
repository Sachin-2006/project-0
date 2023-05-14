from django.urls import path , include
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/<str:username>/" , ChatConsumer.as_asgi()) ,
]
