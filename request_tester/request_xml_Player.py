import requests                        # Bibliothek die es uns ermöglicht HTTP-Anfragen zu senden und zu empfangen
from xml.etree import ElementTree      # Bibliothek die es uns ermöglicht XML zu lesen und zu schreiben
from xml.dom import minidom            # Bibliothek die es uns ermöglicht XML zu formatieren (hübsch zu machen) 

#--------------------------------------------------------------------------------------------------------------------------------
# Diese Datei dient zum Auswerten des XML-Requests für die BeachTournament Liste.
# Die BeachTournament Liste wird benötigt um die BeachTournaments in der Datenbank zu speichern
#Einstiegspunkt  für alle Web Service XML Requests:
# https://www.fivb.org/vis2009/XmlRequest.asmx

#--------------------------------------------------------------------------------------------------------------------------------

# URL und Payload definieren
url = "https://www.fivb.org/vis2009/XmlRequest.asmx"
payload = {
    "Request": "<Request Type='GetPlayerList' Fields='FederationCode FirstName Gender LastName  PlaysBeach PlaysVolley TeamName No Version'></Request>"
}

# HTTP-Anfrage senden und Antwort empfangen (response)

response = requests.get(url, params=payload)
print(response.status_code)
print(response.content)


# Überprüfen ob die Anfrage erfolgreich war (Status Code 200)
if response.status_code == 200:

    # Die XML aus der Antwort auslesen
    # (ElementTree.fromstring() erwartet einen String, deshalb müssen wir response.content in einen String umwandeln)
    xml_response = ElementTree.fromstring(response.content)
    
    # Die XML formatieren (hübsch machen)
    # (ElementTree.tostring() erwartet ein Element, deshalb müssen wir xml_response übergeben)

    rough_string = ElementTree.tostring(xml_response, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml_str = reparsed.toprettyxml(indent="  ")
    
    # Die formatierte XML in eine Datei schreiben (BeachTournamentList.xml)
    
    with open("PlayerList.xml", "w", encoding="UTF-8") as file:
        file.write(pretty_xml_str)
else:
    print(f"FAILED to retrieve the Data: {response.status_code}")