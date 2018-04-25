""" modelo URL Configuration """

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^bolsa/', include('modelo.bolsa.urls', namespace='modelo-bolsa')),
    url(r'^bookings/', include('modelo.bookings.urls', namespace='modelo-bookings')),
    url(r'^api/bookings/', include('modelo.bookings.api.urls', namespace='booking-api')),
    path('admin/', admin.site.urls),
]
