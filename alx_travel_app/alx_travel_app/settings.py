import environ
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')
app = Celery('alx_travel_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
env = environ.Env()
environ.Env.read_env()  # reads .env file

SECRET_KEY = env('SECRET_KEY', default='dummy_secret_key')
DEBUG = env.bool('DEBUG', default=True)
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

