from django.contrib import admin

from .models import Trip, MyTrips, MyTrip

admin.site.register(Trip)
admin.site.register(MyTrips)
admin.site.register(MyTrip)
