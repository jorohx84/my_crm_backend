import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # User-ID aus der URL
        print("Trying to connect", self.scope['url_route']['kwargs'])
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.group_name = f'notifications_{self.user_id}'

        # User-Group joinen
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Verbindung akzeptieren
        await self.accept()

    async def disconnect(self, close_code):
        # User-Group verlassen
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Methode, die Nachrichten aus dem Signal empfängt
    async def send_notification(self, event):
        # event['message'] wird aus dem Signal gesendet
        await self.send(text_data=json.dumps(event['message']))


    async def connect(self):
        print("🌐 Connect attempt from:", self.scope)
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.group_name = f'notifications_{self.user_id}'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()