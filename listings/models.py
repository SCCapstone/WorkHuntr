from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
import random
import string

STATUSES = [
    ('Strutting', 'Strutting'),
    ('Spotted', 'Spotted'),
    ('Claimed', 'Claimed'),
    ('Completed', 'Completed')
]

TAGS = [
    ('NONE', 'NONE'),
    ('AI', 'AI'),
    ('DEVELOPMENT', 'DEVELOPMENT'),
    ('DESIGN', 'DESIGN'), 
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('Python', 'Python'),
    ('Web', 'Web')
]

class Listings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUSES, default='Strutting')
    tag1 = models.CharField(max_length=11, choices=TAGS, default='NONE', verbose_name='TAG ONE')
    tag2 = models.CharField(max_length=11, choices=TAGS, default='NONE', verbose_name='TAG TWO')
    tag3 = models.CharField(max_length=11, choices=TAGS, default='NONE', verbose_name='TAG THREE')
    huntee = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='huntee')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='hunter')
    
    def __str__(self):
        return self.title


