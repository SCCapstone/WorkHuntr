from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def create_profile(sender, instance, created, **kwargs):
  print('REACHED SIGNAL')
  user = instance
  if created:
    profile = Profile(user=user)
    profile.save()
    print('REACHED CREATED')
  instance.profile.save()
  print('REACHED SAVED')
