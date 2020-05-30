import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


class DoulixConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = 'doulix'

        # joing doulix group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # leave from group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # send message to the group
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message
            }
        )

        # receive message from room group
    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
