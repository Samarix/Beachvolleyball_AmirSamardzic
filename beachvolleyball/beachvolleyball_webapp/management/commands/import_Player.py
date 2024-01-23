from django.core.management.base import BaseCommand
from xml.etree import ElementTree
import requests

from beachvolleyball_webapp.models import Player

class Command(BaseCommand):
    help = 'Importiere BeachRounds aus XML-Datei'

    def handle(self, *args, **kwargs):
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"
        payload = {
        "Request": "<Request Type='GetPlayerList' Fields='FederationCode FirstName Gender LastName  PlaysBeach PlaysVolley TeamName No Version'></Request>"
        }

      
        # HTTP-Anfrage senden und Antwort empfangen (response)
        response = requests.get(url, params=payload)
        print(response.status_code)
        #print(response.content) # gibt die Antwort als Byte-Objekt aus
        # Überprüfen ob die Anfrage erfolgreich war (Status Code 200)

        if response.status_code == 200:
            # Die XML aus der Antwort auslesen
            xml_response = ElementTree.fromstring(response.content)
            # Die Events aus der XML auslesen
            

            for player in xml_response.findall('Player'):
                FederationCode = player.attrib.get('FederationCode')
                FirstName = player.attrib.get('FirstName')
                Gender = player.attrib.get('Gender')
                LastName = player.attrib.get('LastName')
                PlaysBeach = player.attrib.get('PlaysBeach')
                PlaysVolley = player.attrib.get('PlaysVolley')
                TeamName = player.attrib.get('TeamName')
                No = player.attrib.get('No')
                Version = player.attrib.get('Version')




                Player.objects.get_or_create(
                    No=No,
                    defaults={
                        'FederationCode': FederationCode,
                        'FirstName': FirstName,
                        'Gender': Gender,
                        'LastName': LastName,
                        'PlaysBeach': PlaysBeach,
                        'PlaysVolley': PlaysVolley,
                        'TeamName': TeamName,
                        'Version': Version,
                    }
                )       
   
# Unterschied zwischen get_or_create und update_or_create
# Antwort: get_or_create erstellt einen neuen Eintrag in der Datenbank, wenn es den Eintrag noch nicht gibt.

# Wozu wird das default={} benötigt?
# Antwort: Damit wird der Eintrag in der Datenbank mit den Werten aus default={} erstellt, wenn es den Eintrag noch nicht gibt.
                
                



