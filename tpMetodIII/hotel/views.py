from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from hotel.models import *
from random import randint
import datetime

# Create your views here.


def index(request):
    ownerships = Ownership.objects.all()  # me traigo todas las propiedades y no importa si no hay ninguna
    context = {
        'ownerships': ownerships
    }

    return render(request, 'hotel/home.html', context)


def ownership_details(request, ownership_id, message=None):

    ownership = get_object_or_404(Ownership, pk=ownership_id)
    rental_dates = RentalDate.objects.filter(ownership_id=ownership_id, booked=None);
    print(rental_dates)
    context = {
        'ownership': ownership,
        'rental_dates': rental_dates,
        'message': message
    }
    return render(request, 'hotel/ownership_details.html', context)


def book(request):  # todavia hay que completar el metodo
    if request.method == "POST":
        query_dict = request.POST

        dates = query_dict.getlist('date[]')

        ownership_id = query_dict.get('ownership_id')

        client_name = query_dict.get('name')
        client_lastname = query_dict.get('lastname')
        client_email = query_dict.get('email')

        book_number = randint(1000, 9999)
        booked = Book(date=datetime.datetime.now(), client_name=client_name, client_lastname=client_lastname,
                      client_email=client_email, book_number=book_number)
        booked.save()
        for date in dates:
            rental_date = RentalDate.objects.get(pk=date)
            if rental_date.booked:  # aca deberiamos arreglarlo
                return ownership_details(request, str(ownership_id), {
                        'type': 'danger',
                        'text': 'No se pudo reservar: Hay una fecha %s esta reservada.' % rental_date.booked.date
                })

            # falta completar campo book_number , deberia ser aleatorio

            rental_date.booked = booked
            rental_date.save()

        return ownership_details(request, str(ownership_id), {
                'type': 'success',
                'text': 'Reservado con exito !'
        })
