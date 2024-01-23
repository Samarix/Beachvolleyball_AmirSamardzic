from django.core.management.base import BaseCommand
from xml.etree import ElementTree
import requests
from datetime import datetime

from beachvolleyball_webapp.models import Event

class Command(BaseCommand):
    help = 'Importiere Events aus XML-Datei'

    def handle(self, *args, **kwargs):
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"
        payload = {
            "Request": "<Request Type='GetEventList' Fields='Code Name StartDate EndDate No Version'>"
                    "<Filter IsVisManaged='True' NoParentEvent='0' HasBeachTournament='True' /></Request>"

        }

        try:
            # HTTP-Anfrage senden und Antwort empfangen (response)
            response = requests.get(url, params=payload)
            print(response.status_code)
            print(response.content) # gibt die Antwort als Byte-Objekt aus
            # Überprüfen ob die Anfrage erfolgreich war (Status Code 200)

            if response.status_code == 200:
                # Die XML aus der Antwort auslesen
                xml_response = ElementTree.fromstring(response.content)
                # Die Events aus der XML auslesen

                for event in xml_response.findall('Event'):
                    print("test1")
                    # Die Daten aus der XML auslesen
                    Code = event.get('Code')
                    Name = event.get('Name')
                    StartDate = event.get('StartDate')
                    EndDate = event.get('EndDate')
                    No = event.get('No')
                    Version = event.get('Version')
                    

                    Event.objects.update_or_create(
                    Code=Code,
                    Name=Name,
                    StartDate=datetime.strptime(StartDate, '%Y-%m-%d'),
                    EndDate=datetime.strptime(EndDate, '%Y-%m-%d'),
                    no=No,
                    Version=Version
                    )
                    
        except:
            print("Fehler beim Importieren der Events")
            return
        
       





