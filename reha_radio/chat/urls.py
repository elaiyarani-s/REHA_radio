from django.urls import path
from .views import chat_page

urlpatterns = [
    path('chat/', chat_page, name='chat'),  # Enables {% url 'chat' %}
]
