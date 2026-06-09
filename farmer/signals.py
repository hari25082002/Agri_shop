from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Farmer_profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        Farmer_profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    farmer_profile = getattr(instance, 'farmer_profile', None)
    if farmer_profile:
        farmer_profile.save()
