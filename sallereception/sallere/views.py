from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Gestion de la salle de réception OASI Y'AMAHORO")
