import os
import sys

path='/var/www/arq_chat'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'arq_chat.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
