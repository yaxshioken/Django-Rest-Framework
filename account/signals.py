from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Profile, User


@receiver(signal=post_save, sender=User)
def create_account_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
