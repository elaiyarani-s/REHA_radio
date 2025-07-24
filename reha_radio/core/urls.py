from django.urls import path, include
from . import views 

urlpatterns = [

    path('station/<int:station_id>/', views.station_detail_view, name='station_detail'),
]