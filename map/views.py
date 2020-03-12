from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

# Create your views here.
from .models import Parking
from .forms import ScheduleForm

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

def get_parking_info(request):
    # request debe ser AJAX y metodo GET.
    if  request.is_ajax and request.method == "GET":
        # get parking_id del lado del cliente
        parking_id = request.GET.get("parking_id", None)
        # get parking from DB
        parking = Parking.objects.filter(id = parking_id).first()
        # serializar en JSON el parking
        ser_parking = serializers.serialize('json', [ parking, ])
        # envio al cliente
        return JsonResponse({"parking": ser_parking}, status = 200)
    
    return JsonResponse({}, status = 400)

def make_schedule(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScheduleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('map')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScheduleForm()

    return render(request, 'map/schedule.html', {'form': form})
