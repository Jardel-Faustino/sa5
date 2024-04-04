"""
Configuração WSGI para projeto globaltalent_connect.

Ele expõe o WSGI que pode ser chamado como uma variável de nível de módulo chamada ``application``.

Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaltalent_connect.settings')

application = get_wsgi_application()
