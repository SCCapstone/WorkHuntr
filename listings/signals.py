from django.contrib.auth.models import Listings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Listings

@receiver(post_save, sender=Listings, dispatch_uid='save_new_listing')
def create_listing(sender, instance, created, **kwargs):
  listing = instance
  if created:
    listing.save()
  instance.listing.save()