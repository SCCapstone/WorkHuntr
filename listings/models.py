import datetime

from django.db import models
from django.utils import timezone
import random
import string
# Create your models here.

class Listings(models.Model):
    STATUSES = [
        ('Strutting', 'Strutting'),
        ('Spotted', 'Spotted'),
        ('Claimed', 'Claimed'),
        ('Completed', 'Completed')
    ]

    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    #status = models.CharField(max_length=10, choices=STATUSES, default='Strutting')

    def __str__(self):
        return self.title


