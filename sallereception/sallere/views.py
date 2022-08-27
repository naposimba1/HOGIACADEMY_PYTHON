from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Reservation

# Create your views here.
# def index(request):
#  return HttpResponse("Gestion de la salle de réception OASI Y'AMAHORO")


def index(request):
    # reservations = Reservation.objects.all() ni cokimwe na select * from Reservation muri sql
    reservations = Reservation.objects.all()
    total = 0
    for x in reservations:
        total = total+x.a_payer
    return render(request, 'index.html', {
        'reservations': reservations,
        'total': total
    })
