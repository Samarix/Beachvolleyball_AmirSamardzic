from django.core.management.base import BaseCommand
from xml.etree import ElementTree
import requests
from datetime import datetime

from beachvolleyball_webapp.models import BeachRound

class Command(BaseCommand):
    help = 'Importiere BeachRounds aus XML-Datei'

    def handle(self, *args, **kwargs):
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"
        payload = {
        "Request": "<Requests> <Request Type='GetBeachRoundList' Fields='Code Name Bracket Phase StartDate EndDate No Version'> </Request> </Requests>"
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
            

            for beachround in xml_response.findall('.//BeachRound'):
                Code = beachround.attrib.get('Code')
                Name = beachround.attrib.get('Name')
                Bracket = beachround.attrib.get('Bracket')
                Phase = beachround.attrib.get('Phase')
                StartDate = beachround.attrib.get('StartDate')
                EndDate = beachround.attrib.get('EndDate')
                No = beachround.attrib.get('No')
                Version = beachround.attrib.get('Version')

                BeachRound.objects.get_or_create(
                    No=No,
                    defaults={
                        'Code': Code,
                        'Name': Name,
                        'Bracket': Bracket,
                        'Phase': Phase,
                        'StartDate': datetime.strptime(StartDate, '%Y-%m-%d') if StartDate else None,
                        'EndDate': datetime.strptime(EndDate, '%Y-%m-%d') if EndDate else None,
                        'Version': Version,
                    }
                )       
   



