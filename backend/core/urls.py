from django.urls import path, include
from . import views 

urlpatterns = [

    path('', views.home, name='home'),
    path('station/<int:station_id>/', views.station_detail_view, name='station_detail'),
]