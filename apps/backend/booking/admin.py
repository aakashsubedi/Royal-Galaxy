from django.contrib import admin
from .models import *


class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'booking_date', 'arrival_date', 'type', 'room']
    search_fields = ['first_name', 'last_name', 'type', 'room']
    list_display_links = ['first_name', 'last_name']
    list_filter = ['type', 'room']


admin.site.register(Booking, BookingAdmin)
