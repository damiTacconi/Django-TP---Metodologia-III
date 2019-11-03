from django.shortcuts import render, get_list_or_404
from hotel.models import *

# Create your views here.


def index(request):
    cities = get_list_or_404(City)
    return render(request, 'hotel/home.html', {'cities': cities})
