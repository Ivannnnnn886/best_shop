from django.shortcuts import render, redirect

from .forms import ReservationForm
from .models import Category,Gallery, Event, Reservation
from django.db import models
from django.utils.timezone import now

def reservation_success(request):
    return render(request,'reservation_success.html')



# Create your views here.
def home(request):
    form = ReservationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('reservation_success')


    categories = Category.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    events = Event.objects.filter(models.Q(date_time__isnull=True) | models.Q(date_time__gte=now())).filter(is_visible=True)



    context = {
        'categories': categories,
        'gallery': gallery,
        'events': events,
        'reservation_form': form,
    }
    return render(request, 'main.html', context=context)

