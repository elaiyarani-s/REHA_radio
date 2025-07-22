# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
from django.core.cache import cache
import hashlib

def nickname_to_color(nickname):
    colors = [
        "#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231",
        "#911eb4", "#46f0f0", "#f032e6", "#bcf60c", "#fabebe",
        "#008080", "#e6beff", "#9a6324", "#fffac8", "#800000",
        "#aaffc3", "#808000", "#ffd8b1", "#000075", "#808080"
    ]
    # Use hash to pick a color index
    h = int(hashlib.md5(nickname.encode()).hexdigest(), 16)
    return colors[h % len(colors)]


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'public_chat'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        nickname = data.get('nickname', 'Anonymous')
        timestamp = datetime.now().strftime('%H:%M:%S')
        color = nickname_to_color(nickname)  # assign color

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'nickname': nickname,
                'timestamp': timestamp,
                'color': color,
            }
        )

    def assign_color(self, nickname):
        # Consistent color per nickname using hash
        import hashlib
        hex_digest = hashlib.md5(nickname.encode()).hexdigest()
        return f"#{hex_digest[:6]}"  # first 6 hex digits

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'nickname': event['nickname'],
            'timestamp': event['timestamp'],
            'color': event['color'],
        }))
