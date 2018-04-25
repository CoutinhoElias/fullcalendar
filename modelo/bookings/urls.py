from django.conf.urls import url, include
from django.views.i18n import JavaScriptCatalog

from modelo.bookings.views import list, scheduling, scheduling_edit, bookings_create

app_name = 'bookings'

urlpatterns = [
    url(r'listagem/$', list, name='list'),
    url(r'agendamento/$', scheduling, name='scheduling'),
    url(r'agendamento/novo/$', bookings_create, name='bookings_create'),
    url(r'reserva/editar/(?P<id_booking>\d+)/$', scheduling_edit, name='scheduling_edit'),
    
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
