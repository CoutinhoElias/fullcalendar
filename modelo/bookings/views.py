from datetime import date

from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from rest_framework.viewsets import ModelViewSet

from modelo.bookings.forms import BookingsForm
from modelo.bookings.models import Booking
from modelo.bookings.serializer import BookingSerializer



class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def list(request):
    selected_date = date.today()
    return list_date(request) #return list_date(request, selected_date.year, selected_date.month)


def list_date(request):
    return render(request, 'bookings/bookings_list.html') #def list_date(request, year, month):

# def bookings_create(request):
# 	if request.method == 'POST':
# 		form = BookingsForm(request.POST)
# 	else:
# 		form = BookingsForm()
# 	return save_all(request,form,'book_create.html')

def bookings_create(request):
    data = dict()

    if request.method == 'POST':
        form = BookingsForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = BookingsForm()
    context = {'form': form}
    data['html_form'] = render_to_string('bookings_create_form.html',
        context,
        request=request
    )
    return JsonResponse(data)


def scheduling(request):
    if request.method == 'POST':
        form = BookingsForm(request.POST)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            form.save_m2m()

            return HttpResponseRedirect('bookings/listagem/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            return render(request, 'bookings/scheduling_form.html', {'form':form})
    else:
        context = {'form': BookingsForm()}
        return render(request, 'bookings/scheduling_form.html', context)


def scheduling_edit(request, id_booking):
    booking = Booking.objects.get(id=id_booking)
    if request.method == 'GET':
        form = BookingsForm(instance=booking)
    else:
        form = BookingsForm(request.POST, instance=booking)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            form.save_m2m()
        return HttpResponseRedirect('bookings/listagem/'+id_booking)
    return render(request, 'bookings/scheduling_form.html', {'form': form})

