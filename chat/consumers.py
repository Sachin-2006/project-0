import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from core.models import User
from asgiref.sync import sync_to_async
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]['kwargs']['username']
        self.chat_room_name = 'chat_%s'%self.room_name
        await self.channel_layer.group_add(
            self.chat_room_name ,
            self.channel_name
        )
        await self.accept()
        


    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.chat_room_name ,
            self.channel_layer
        )
        raise StopConsumer()
    
    async def receive(self, text_data):
        print(self.chat_room_name)
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]
        receiver = text_data_json["receiver"]
        receiver_user = await get_receiver(receiver)
        sender_user = await get_receiver(sender)
        self.receiver_user = receiver_user
        self.sender_user = sender_user

        if sender_user.id < receiver_user.id:
            room_name = "chat"+str(sender_user)+"_"+str(receiver_user)
        else:
            room_name = "chat"+str(receiver_user)+"_"+str(sender_user)
        await create_message(sender_user,receiver_user,room_name,message)

        await self.channel_layer.group_send(
            self.chat_room_name,{
                "type" : "sendMessage" ,
                "message" : message ,
                "sender" : sender ,
                "receiver":receiver,
            })
    async def sendMessage(self , event) :
        print(1)
        print(event)
        message = event["message"]
        sender = event["sender"]
        receiver = event["receiver"]

        await self.send(text_data = json.dumps({"message":message ,"sender":sender,"receiver":receiver}))
    @database_sync_to_async
    def get_last_posts(self):
        if self.sender_user.id < self.receiver_user.id:
            room_name = "chat"+str(self.sender_user)+"_"+str(self.receiver_user)
        else:
            room_name = "chat"+str(self.receiver_user)+"_"+str(self.sender_user)

        messages = Message.objects.filter(room_name=room_name)


@database_sync_to_async
def create_message(sender,receiver,room_name,message):
    message = Message(sender=sender,receiver=receiver,room_name=room_name,message=message)
    message.save()

 
@database_sync_to_async
def get_receiver(name):
    u = User.objects.get(username=name)
    return u