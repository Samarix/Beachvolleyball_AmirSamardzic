from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
 path ('', views.home, name = 'home'),
 path ('events/', views.events, name = 'events'),
 path ('beachtournaments/', views.beachtournaments, name = 'beachtournaments'),
 
]

#-------------------------------------------------------------------------------------------------------------------------

#URL Patterns in Django sind ein Weg, um URLs mit den Views(Ansichten) in Ihrem Django-Projekt zu verknüpfen. 
#Dieses Mapping zwischen URLs und Ansichten wird in einer Datei mit dem Namen urls.py gespeichert.
# Django führt eine URL-Übereinstimmung von oben nach unten durch und hört auf, sobald es eine Übereinstimmung findet.

#URL-Patterns ermöglichen es uns, Routen für unsere Anwendung zu definieren.
#Dies sind Pfade, die Benutzer in der Adressleiste ihres Browsers eingeben, um zu einer bestimmten Seite zu gelangen.

#--------------------------------------------------------------------------------------------------------------------------
