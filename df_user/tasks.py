from celery import task
from dailifresh import settings
from django.core.mail import send_mail
import time

@task
def send_email(name, email):
    message = '<h1>欢迎你加入dailyfresh大家庭</h1><br>'+name
    send_mail('欢迎信息', '', settings.EMAIL_FROM, [email], html_message=message)
    time.sleep(3)