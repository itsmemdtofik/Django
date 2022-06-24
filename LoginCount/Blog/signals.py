from tabnanny import verbose
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache
from importlib_metadata import version

@receiver(user_logged_in, sender = User)
def LoginSuccess(sender, request, user, **kwargs):
    myCount = cache.get('count', 0, version = user.pk)
    newCount = myCount + 1
    cache.set('count', newCount, 60 * 60 * 24, version = user.pk)
    print(user.pk)