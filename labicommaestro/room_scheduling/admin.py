from django.contrib import admin

from models import Room, Reservation

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', )

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('event_name', )

admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)


# Register your models here.
