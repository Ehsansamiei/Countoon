from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Token
import secrets


@receiver(post_save, sender=User)
def create_token_for_user(sender, instance, created, **kwargs):
    if created:
        token_value = secrets.token_urlsafe(32)
        Token.objects.create(user=instance, token = token_value)