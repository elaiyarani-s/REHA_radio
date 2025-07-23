# your_project/routing.py
from django.urls import re_path
from chat.consumers import ChatConsumer, AdminChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),  # public
    re_path(r'ws/private/(?P<nickname>\w+)/$', ChatConsumer.as_asgi()),  # private
    re_path(r'ws/admin/$', AdminChatConsumer.as_asgi()),  # admin
]
