from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from main.models import Reservation

def is_manager(user):
    return user.groups.filter(name='manager').exists() or user.is_superuser


# Create your views here.
@login_required(login_url='login')
@user_passes_test(is_manager)
def booking_data(request):
    data = Reservation.objects.filter(is_confirmed=False)
    context = {'items': data}
    return render(request, 'reservations.html', context=context)


def booking_confirm(request, pk):
    data = Reservation.objects.get(pk=pk)
    data.is_confirmed = True
    data.save()
    return redirect('manager:booking')
