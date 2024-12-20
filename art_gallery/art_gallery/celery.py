import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'art_gallery.settings')

app = Celery('art_gallery')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task-every-10-seconds': {
        'task': 'user.tasks.send_message',  
        'schedule': 1,  

    },
    'task-every-morning': {
        'task': 'user.tasks.send_message',
        'schedule': crontab(hour=8, minute=0),  
    },
}
