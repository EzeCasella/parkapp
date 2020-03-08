from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
from .models import Parking

def index(request):
    return render(request, 'map/index.html')

def map(request):

    parkings_list = Parking.objects.all()
    context = {
        'parkings_list': parkings_list ,
        # 'parkings_list': json.dumps("json", parkings_list) ,
    }
    return render(request, 'map/map.html', context)