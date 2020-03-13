from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.template.loader import render_to_string

# Create your views here.
from .models import Parking, Schedule
from .forms import ScheduleForm

def index(request):
    # return render(request, 'index.html')
    return redirect('map')

def map(request):
    form = ScheduleForm()
    parkings_list = Parking.objects.all()
    context = {
        'parkings_list': parkings_list ,
        # 'parkings_list': json.dumps("json", parkings_list) ,
        'form':form,
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

def make_schedule(request, parking_id=None):
    # if this is a POST request we need to process the form data
    if request.is_ajax and request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScheduleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # schedule = Schedule()
            parking = Parking.objects.filter(id = parking_id).first()

            sched = Schedule(
                parking = parking,
                checkin_date = form.cleaned_data['checkin_date'],
                checkin_time = form.cleaned_data['checkin_time'],
                checkout_date = form.cleaned_data['checkout_date'],
                checkout_time = form.cleaned_data['checkout_time'],
                phone_number = form.cleaned_data['phone_number'],
            )
            sched.save()
            return redirect('map')

    # if a GET (or any other method) we'll create a blank form
    elif  request.is_ajax and request.method == "GET":
        # get parking_id del lado del cliente
        parking_id = request.GET.get("parking_id", None)
        # get parking from DB
        if Parking.objects.filter(id = parking_id).exists():

            parking = Parking.objects.filter(id = parking_id).first()
            parking_name = parking.name

            form = ScheduleForm()
            rendered_form = render_to_string('map/schedule.html', request=request, context={'form': form, 'parking_id':parking_id})

            return JsonResponse({"parking_name": parking_name, 'form': rendered_form}, status = 200)

    return JsonResponse({}, status = 400)

    return render(request, 'map/schedule.html', {'form': form})
