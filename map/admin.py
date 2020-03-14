from django.contrib import admin

# Register your models here.

from .models import Parking, Schedule

class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 0


class ParkingAdmin (admin.ModelAdmin):
    list_display = ('name', 'hourRate', 'address', 'phoneNumber', 'carSlots', 'openingHours', 'notes')
    search_fields = ['name']

    inlines = [ScheduleInline]

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'parking')
    list_display = ('id', 'parking', 'checkin_date', 'checkin_time', 'checkout_date', 'checkout_time', 'phone_number' )
    
    list_filter = ['checkin_date', 'parking']

    fieldsets = [
        ('Schedule',               {'fields': ['id', 'parking']}),
        ('Date Information', {'fields':['checkin_date', 'checkin_time', 'checkout_date', 'checkout_time']}),
        ('Contact Information', {'fields': ['phone_number']})
    ]
    


admin.site.register( Parking, ParkingAdmin)