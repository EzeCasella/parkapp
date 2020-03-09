from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
from .models import Parking

def index(request):
    # return render(request, 'index.html')
    return redirect('map')

def map(request):

    parkings_list = Parking.objects.all()
    context = {
        'parkings_list': parkings_list ,
        # 'parkings_list': json.dumps("json", parkings_list) ,
    }
    return render(request, 'map/map.html', context)

def detail(request, parking_id):
    sel_parking = get_object_or_404(Parking, pk=parking_id)
    parkings_list = Parking.objects.all()
    context = {
        'parkings_list': parkings_list ,
        # 'parkings_list': json.dumps("json", parkings_list) ,
        'sel_parking': sel_parking 
    }
    return render(request, 'map/map.html', context)