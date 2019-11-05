from django.shortcuts import render, get_list_or_404
from hotel.models import *

# Create your views here.


def index(request):
    cities = get_list_or_404(City) # me traigo todas las ciudades y si no hay ninguna lanzo error 404
    ownerships = Ownership.objects.all() # me traigo todas las propiedades y no importa si no hay ninguna
    context = {
        'cities': cities,
        'ownerships': ownerships
    }

    return render(request, 'hotel/home.html', context)
