"""
WSGI config for beachvolleyball project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beachvolleyball.settings')

application = get_wsgi_application()

#-------------------------------------------------------------------------------------------------------------------------
#Die WSGI-Schnittstelle fungiert als Brücke zwischen dem Webserver (z. B. Apache oder Nginx) und der Django-Anwendung. 
#Sie definiert, wie der Webserver Anfragen an die Anwendung weiterleitet und wie die Anwendung die Anfragen verarbeitet
# und Antworten zurück an den Webserver sendet
#--------------------------------------------------------------------------------------------------------------------------