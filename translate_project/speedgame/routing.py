from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/speedgame/<int:room_pk>/", consumers.SpeedgameConsumer.as_asgi()),
]