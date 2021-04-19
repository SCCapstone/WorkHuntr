from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Code, Profile

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()
    instance.profile.save()

@receiver(post_save, sender=User)
def generate_code(sender, instance, created, **kwargs):
    user = instance
    if created:
        code = Code(user=user)
        code.save()
    instance.code.save()