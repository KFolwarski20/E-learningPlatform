import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Akceptacja połączenia.
        self.accept()

    def disconnect(self, close_code):
        pass

    # Odbiór komunikatu WebSocket.
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # Wysyłanie komunikatu do WebSocket.
        self.send(text_data=json.dumps({"message": message}))
