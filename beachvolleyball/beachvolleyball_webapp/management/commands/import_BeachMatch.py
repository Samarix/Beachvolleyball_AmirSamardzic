from django.core.management.base import BaseCommand
from xml.etree import ElementTree
import requests
from datetime import datetime

from beachvolleyball_webapp.models import BeachMatch

class Command(BaseCommand):
    help = 'Importiere BeachRounds aus XML-Datei'

    def handle(self, *args, **kwargs):
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"
        payload = {
        "Request": "<Request Type='GetBeachMatchList' Fields='NoInTournament LocalDate LocalTime NoTeamA NoTeamB Court \
        MatchPointsA MatchPointsB PointsTeamASet1 PointsTeamBSet1 PointsTeamASet2 PointsTeamBSet2 PointsTeamASet3 PointsTeamBSet3 \
        DurationSet1 DurationSet2 DurationSet3 No Version'></Request>"
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
            
            #        payload = {
        # "Request": "<Request Type='GetBeachMatchList' Fields='NoInTournament LocalDate LocalTime NoTeamA NoTeamB Court \
        # MatchPointsA MatchPointsB PointsTeamASet1 PointsTeamBSet1 PointsTeamASet2 PointsTeamBSet2 PointsTeamASet3 PointsTeamBSet3 \
        # DurationSet1 DurationSet2 DurationSet3 No Version'></Request>"
        # }

            for beachmatch in xml_response.findall('BeachMatch'):
                NoInTournament = beachmatch.attrib.get('NoInTournament')
                LocalDate = beachmatch.attrib.get('LocalDate')
                LocalTime = beachmatch.attrib.get('LocalTime')
                NoTeamA = beachmatch.attrib.get('NoTeamA')
                NoTeamB = beachmatch.attrib.get('NoTeamB')
                Court = beachmatch.attrib.get('Court')
                MatchPointsA = beachmatch.attrib.get('MatchPointsA')
                MatchPointsB = beachmatch.attrib.get('MatchPointsB')
                PointsTeamASet1 = beachmatch.attrib.get('PointsTeamASet1')
                PointsTeamBSet1 = beachmatch.attrib.get('PointsTeamBSet1')
                PointsTeamASet2 = beachmatch.attrib.get('PointsTeamASet2')
                PointsTeamBSet2 = beachmatch.attrib.get('PointsTeamBSet2')
                PointsTeamASet3 = beachmatch.attrib.get('PointsTeamASet3')
                PointsTeamBSet3 = beachmatch.attrib.get('PointsTeamBSet3')
                DurationSet1 = beachmatch.attrib.get('DurationSet1')
                DurationSet2 = beachmatch.attrib.get('DurationSet2')
                DurationSet3 = beachmatch.attrib.get('DurationSet3')
                No = beachmatch.attrib.get('No')
                Version = beachmatch.attrib.get('Version')


                BeachMatch.objects.get_or_create(
                    No=No,
                    NoTeamA=NoTeamA,
                    NoTeamB=NoTeamB,
                    defaults={
                        'NoInTournament': NoInTournament,
                        'LocalDate': datetime.strptime(LocalDate, '%Y-%m-%d') if LocalDate else None,
                        'LocalTime': datetime.strptime(LocalTime, '%H:%M:%S') if LocalTime else None,
                        'Court': Court,
                        'MatchPointsA': MatchPointsA,
                        'MatchPointsB': MatchPointsB,
                        'PointsTeamASet1': PointsTeamASet1,
                        'PointsTeamBSet1': PointsTeamBSet1,
                        'PointsTeamASet2': PointsTeamASet2,
                        'PointsTeamBSet2': PointsTeamBSet2,
                        'PointsTeamASet3': PointsTeamASet3,
                        'PointsTeamBSet3': PointsTeamBSet3,
                        'DurationSet1': DurationSet1,
                        'DurationSet2': DurationSet2,
                        'DurationSet3': DurationSet3,
                        'Version': Version,
                    }
                )       
   



