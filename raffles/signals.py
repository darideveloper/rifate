import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

from raffles import models


# Create tickets when save a new raffle
@receiver(post_save, sender=models.Raffle)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        # Run ticket creation in a background thread
        threading.Thread(target=sender.create_tickets, args=(instance,)).start()
