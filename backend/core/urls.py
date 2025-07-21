from django.urls import path, include
from . import views 

urlpatterns = [

    path('stations/', views.station_list_view, name='stations_list'),
    path('station/<int:station_id>/', views.station_detail_view, name='station_detail'),
]