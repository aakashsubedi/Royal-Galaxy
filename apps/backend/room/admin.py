from django.contrib import admin
from .models import *


class RooomAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'type', 'status', 'position']
    search_fields = ['title', 'price', 'type']
    list_display_links = ['title', 'price', ]
    list_filter = ['type']


admin.site.register(Room, RooomAdmin)
admin.site.register(RoomType)
