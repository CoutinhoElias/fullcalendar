from django.contrib import admin
from modelo.bookings.models import Booking


class BookingModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Booking, BookingModelAdmin)
