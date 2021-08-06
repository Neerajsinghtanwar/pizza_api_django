from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from django.core.mail import send_mail
from pizza_api_django.settings import EMAIL_HOST_USER


@receiver(post_save, sender=User)
def email(sender, request, **kwargs):
    subject = "Someone Login On Library"
    message = f"Welcome to Pizza App"
    email_from = EMAIL_HOST_USER
    email = ''
    send_mail(subject, message, email_from, [email], fail_silently=False)
