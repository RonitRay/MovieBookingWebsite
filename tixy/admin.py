from django.contrib import admin
from .models import Movie, Schedule, Slot, Booking

admin.site.register(Movie)
admin.site.register(Schedule)
admin.site.register(Slot)
admin.site.register(Booking)