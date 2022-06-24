from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender = User)
def LoginSuccess(sender, request, user, **kwargs):
    print("---------------------------")
    ip = request.META.get('REMOTE_ADDR')
    print("Client's IP = ", ip)
    print("---------------------------\n")
    request.session['ip'] = ip