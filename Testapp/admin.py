from django.contrib import admin
from .models import *

class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name']

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'building']

class RoomAdmin(admin.ModelAdmin):
    list_display= ['number', 'room_type', 'price']

class BlockedDayAdmin(admin.ModelAdmin):
    list_display = ['day', 'room']

admin.site.register(Building, BuildingAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(BlockedDay, BlockedDayAdmin)
