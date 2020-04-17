from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('map/<int:parking_id>/', views.detail, name='detail'), # Quedó obsoleta porque se utiliza get_parking_info
    path('getParkingInfo', views.get_parking_info, name='get_parking_info'),
    path('newSchedule', views.make_schedule, name='new_schedule'),
    path('postSchedule/<int:parking_id>', views.make_schedule, name='post_schedule'),
    path('confirm_sched', views.confirm_schedule, name='confirm_sched'),
]