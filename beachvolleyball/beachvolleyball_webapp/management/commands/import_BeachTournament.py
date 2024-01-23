from django.core.management.base import BaseCommand
from xml.etree import ElementTree
import requests
from datetime import datetime

from beachvolleyball_webapp.models import BeachTournament

class Command(BaseCommand):
    help = 'Importiere Beachtournament aus XML-Datei'

    def handle(self, *args, **options):
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"
        payload = {
        "Request": "<Request Type='GetBeachTournamentList' Fields='Code Name StartDateMainDraw EndDateMainDraw FederationCode No Version'></Request>"
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
            

            for tournament in xml_response.findall('BeachTournament'):
                code = tournament.attrib.get('Code')
                name = tournament.attrib.get('Name')
                start_date_str = tournament.attrib.get('StartDateMainDraw')
                end_date_str = tournament.attrib.get('EndDateMainDraw')
                federation_code = tournament.attrib.get('FederationCode')
                no = tournament.attrib.get('No')
                version = tournament.attrib.get('Version')

           

                BeachTournament.objects.update_or_create(
                    Code=code,
                    defaults={
                         # 'Code' ist der Name des Feldes in der Datenbank, 'code' ist der Wert der Variable 'code
                        'Name': name,
                        'StartDateMainDraw': datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None,
                        'EndDateMainDraw': datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None,
                        'FederationCode': federation_code,
                        'no': no,
                        'Version': version,
                    }
                )
                        
                    
            
                       
                    
   



