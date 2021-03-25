from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile
from .models import Code

@receiver(post_save, sender=User)
def generate_code(sender, instance, created, **kwargs):
    print('reached')
    user = instance
    if created:
        code = Code(user=user)
        code.save()
    instance.code.save()
