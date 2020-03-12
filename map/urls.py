from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('map/<int:parking_id>/', views.detail, name='detail'), # Quedó obsoleta porque se utiliza get_parking_info
    path('ajax/getParkingInfo', views.get_parking_info, name='get_parking_info'),
    path('makeSchedule', views.make_schedule, name='make_schedule')
]