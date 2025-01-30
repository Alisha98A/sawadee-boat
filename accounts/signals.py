from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(email_confirmed)
def activate_user(sender, request, email_address, **kwargs):
    user = email_address.user
    if not user.is_active:
        user.is_active = True
        user.save()