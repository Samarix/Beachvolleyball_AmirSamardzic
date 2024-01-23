# Verwende das offizielle PostgreSQL-Image als Basis
FROM postgres:latest

# Umgebungsvariablen für PostgreSQL-Konfiguration
ENV POSTGRES_DB=beachvolleyball
ENV POSTGRES_USER=beachvolleyball
ENV POSTGRES_PASSWORD=beachvolleyball

# Port, auf dem PostgreSQL lauscht (Standard: 5432)
EXPOSE 5432

# Kopiere lokale SQL-Dateien in den Container (falls erforderlich)
# COPY init.sql /docker-entrypoint-initdb.d/

# Optional: Führe zusätzliche Befehle nach der Containererstellung aus
# Beispiel: Installation von zusätzlichen Paketen
# RUN apt-get update && apt-get install -y some-package

# Optional: Führe zusätzliche Konfigurationen durch
# Beispiel: Ändere die Konfigurationsdatei postgresql.conf
# COPY postgresql.conf /etc/postgresql/postgresql.conf

# Optional: Führe Initialisierungsskripte aus
# Beispiel: Führe Skripte aus, um Datenbank und Benutzer zu erstellen
# COPY init.sql /docker-entrypoint-initdb.d/
