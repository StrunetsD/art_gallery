from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_message():
    send_mail(
        subject='You Are Awesome!',
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['user@example.com'], 
        html_message='<p>Hello!</p><p>You are absolutely awesome!</p>',
    )