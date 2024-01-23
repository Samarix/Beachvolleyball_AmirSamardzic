"""
ASGI config for beachvolleyball project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beachvolleyball.settings')

application = get_asgi_application()

#-------------------------------------------------------------------------------------------------------------------------
#Die asgi.py-Datei in einem Django-Projekt ist ähnlich wie die wsgi.py-Datei, 
#jedoch für die Verwendung von ASGI (Asynchronous Server Gateway Interface). 
#ASGI ist ein Standard für asynchrone Webserver- und Anwendungsschnittstellen in Python, der es ermöglicht,
# Webanwendungen asynchron und effizient zu betreiben.
#--------------------------------------------------------------------------------------------------------------------------
