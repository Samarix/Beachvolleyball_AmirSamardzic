from django.shortcuts import render
from .models import Event, BeachTournament




# Create your views here.

def home(request):
    return render(request, 'home.html', {}) # {} = context

# Context ist ein Wörterbuch, das Variablen enthält die in einer Vorlage verwendet werden.

def events(request):
    events = Event.objects.filter(StartDate__range=["2020-01-01", "2024-12-31"]).order_by('-StartDate')

    context = {
        'events': events,
    }
    
    return render(request, 'events.html', context) 

# Die Render-Funktion wird verwendet, um eine Vorlage mit Daten zu rendern und eine HttpResponse zurückzugeben, die den gerenderten Text enthält.

def beachtournaments(request):

    beachtournaments = BeachTournament.objects

    context = {
        'beachtournaments': beachtournaments,
    }
    return render(request, 'beachtournaments.html', context)
