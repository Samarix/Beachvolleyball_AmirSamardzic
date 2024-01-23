from django.core.management.base import BaseCommand
from xml.etree import ElementTree
import requests


from beachvolleyball_webapp.models import BeachTeam

class Command(BaseCommand):
    help = 'Importiere BeachRounds aus XML-Datei'

    def handle(self, *args, **kwargs):
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"
        payload = {
        "Request": "<Request Type='GetBeachTeamList' Fields='NoPlayer1 NoPlayer2 Name Rank EarnedPointsTeam EarningsTeam No Version'></Request>"
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
            

            for beachteam in xml_response.findall('BeachTeam'):
                if beachteam.attrib.get('NoPlayer1') == '117594':
                    #dann den Eintrag nicht in die Datenbank schreiben
                    #wie geht das?
                    continue # springt zum nächsten Eintrag
                if beachteam.attrib.get('NoPlayer2') == '118824':
                    continue
                NoPlayer1 = beachteam.attrib.get('NoPlayer1')
                NoPlayer2= beachteam.attrib.get('NoPlayer2')
                Name = beachteam.attrib.get('Name')
                Rank = beachteam.attrib.get('Rank')
                EarnedPointsTeam = beachteam.attrib.get('EarnedPointsTeam')
                EarningsTeam = beachteam.attrib.get('EarningsTeam')
                No = beachteam.attrib.get('No')
                Version = beachteam.attrib.get('Version')




                BeachTeam.objects.get_or_create(
                    No=No,
                    defaults={
                    'NoPlayer1':NoPlayer1,
                    'NoPlayer2':NoPlayer2,
                        'Name': Name,
                        'Rank': Rank,
                        'EarnedPointsTeam': EarnedPointsTeam,
                        'EarningsTeam': EarningsTeam,
                        'Version': Version,
                    }
                )     
   



