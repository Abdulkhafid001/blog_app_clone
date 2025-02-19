from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from api.models import Author, Follow

from django.contrib.auth.models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user_for_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(
            user=instance, name=instance.username, email=instance.email)


@receiver(post_save, sender=Follow)
def follow_notification(sender, instance, created, **kwargs):
    if created:
        print(
            f"{instance.follower.name} started following {instance.followed.name}")
