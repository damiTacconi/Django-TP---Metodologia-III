from django.shortcuts import render, get_object_or_404
from hotel.models import *

# Create your views here.


def index(request):
    ownerships = Ownership.objects.all() # me traigo todas las propiedades y no importa si no hay ninguna
    context = {
        'ownerships': ownerships
    }

    return render(request, 'hotel/home.html', context)


def ownership_details(request, ownership_id):

    ownership = get_object_or_404(Ownership, pk=ownership_id)
    rental_dates = RentalDate.objects.filter(ownership_id=ownership_id, booked=None);
    context = {
        'ownership':ownership,
        'rental_dates':rental_dates
    }
    return render(request, 'hotel/ownership_details.html', context);

