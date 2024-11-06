from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Check if the profile does not exist before creating
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        # Attempt to save the profile, but only if it exists
        if hasattr(instance, 'profile'):
            instance.profile.save()
    except Profile.DoesNotExist:
        # Create a profile if it doesn't exist
        Profile.objects.create(user=instance)