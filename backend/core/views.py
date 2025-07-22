import os
import json
from django.conf import settings
from django.shortcuts import render, redirect

def load_stations():
    json_path = os.path.join(settings.BASE_DIR, 'static','data', 'stations.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def station_list_view(request):
    stations = load_stations()
    return render(request, 'core/stations_list.html', {'stations': stations})

def station_detail_view(request, station_id):
    stations = load_stations()
    station = stations.get(str(station_id))
    if not station:
        return redirect('station_list')
    return render(request, 'core/station_detail.html', {'station': station})

# def home(request):
#     return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')