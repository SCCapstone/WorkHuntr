from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
import random
import string

STATUSES = [
    ('Strutting', 'Strutting'),
    ('Claimed', 'Claimed'),
    ('Started', 'Started'),
    ('Milestone 1', 'Milestone 1'),
    ('Milestone 2', 'Milestone 2'),
    ('Milestone 3', 'Milestone 3'),
    ('Complete', 'Complete'),
    ('Payment Issued', 'Payment Issued'),
]

class Listings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    paid_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, default=0, decimal_places=2)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=14, choices=STATUSES, default='Strutting', null=False)
    tag1 = models.CharField(max_length=11, default='NONE', verbose_name='TAG ONE')
    tag2 = models.CharField(max_length=11, default='NONE', verbose_name='TAG TWO')
    tag3 = models.CharField(max_length=11, default='NONE', verbose_name='TAG THREE')
    huntee = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='huntee')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='hunter')

    def __str__(self):
        return self.title


class Update(models.Model):
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=14, choices=STATUSES, default='Started', null=False)
    description = models.CharField(max_length=300, blank=True, null=False)
    listing = models.ForeignKey(Listings, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.status