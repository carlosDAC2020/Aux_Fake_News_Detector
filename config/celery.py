import os
from celery import Celery

# Establece la configuración de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Crea una instancia de Celery
app = Celery('config')

# Configura Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Busca tareas en todos los módulos llamados tasks.py de tu proyecto de Django
app.autodiscover_tasks()
