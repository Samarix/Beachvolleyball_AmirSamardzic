import time                                             # Importiere die time-Bibliothek, um die Wartezeit zu steuern
from django.core.management.base import BaseCommand     # Importiere die BaseCommand-Klasse, um ein eigenes Kommando zu erstellen
from django.db import connections                       # Importiere die connections-Klasse, um die Datenbankverbindung zu überprüfen
from django.db.utils import OperationalError            # Importiere die OperationalError-Klasse, um die Datenbankverbindung zu überprüfen

#----------------------------------------------------------------------------------------------------------------------------------------------

# Erstelle Django Management-Befehl zu erstellen, der darauf wartet,
# dass die Datenbankverbindung verfügbar ist, bevor er den Code ausführt.

# Dieser Befehl wird in der Docker Compose Datei verwendet, um sicherzustellen, dass die Datenbankverbindung verfügbar ist,
# bevor der Code ausgeführt wird, der die Datenbank verwendet.
# Dies ist notwendig, da die Datenbank in einem separaten Container läuft und es einige Zeit dauern kann, bis sie bereit ist.
# Wenn wir den Code ausführen, der die Datenbank verwendet, bevor die Datenbank bereit ist, erhalten wir einen Fehler.


# Dazu verwenden wir die BaseCommand-Klasse, die Django bereitstellt, um eigene Kommandos zu erstellen
# Die BaseCommand-Klasse hat eine handle()-Methode, die wir überschreiben können, um unseren eigenen Code auszuführen
# In diesem Fall warten wir, bis die Datenbankverbindung verfügbar ist, bevor wir weitere Anweisungen ausführen

#----------------------------------------------------------------------------------------------------------------------------------------------


class Command(BaseCommand):
    help = 'Warte auf die Datenbankverbindung'

    def handle(self, *args, **options):
        self.stdout.write('Warten auf die Datenbankverbindung...')

        # Warte, bis die Datenbankverbindung verfügbar ist
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Datenbank nicht verfügbar, warte 1 Sekunde...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Datenbankverbindung ist jetzt verfügbar!'))



