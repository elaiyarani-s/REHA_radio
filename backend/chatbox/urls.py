from django.urls import path, include
from chatbox import views 


urlpatterns = [
    path('chat/<str:room_name>/', views.room, name='room'),
]