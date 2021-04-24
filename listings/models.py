#
# Models for the Listings app
#

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator

# Statuses of a Listing
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

#
# Model for a Listing
#
class Listings(models.Model):
    title = models.CharField(max_length=50, validators=[MaxLengthValidator(50)])
    date = models.DateTimeField(auto_now_add=True)
    paid_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, default=0, decimal_places=2, validators=[MaxValueValidator(999.99), MinValueValidator(0.00)])
    description = models.TextField(max_length=500, validators=[MaxLengthValidator(500)])
    status = models.CharField(max_length=14, choices=STATUSES, default='Strutting', null=False)
    tag_one = models.CharField(max_length=11, default='None')
    tag_two = models.CharField(max_length=11, default='None')
    tag_three = models.CharField(max_length=11, default='None')
    huntee = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='huntee')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='hunter')
    
    # String representation of the Listing model
    def __str__(self):
        return self.title

#
# Model for an update to a Listing
#
class Update(models.Model):
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=14, choices=STATUSES, default='Started', null=False)
    description = models.CharField(max_length=500, blank=True, null=False, validators=[MaxLengthValidator(500)])
    listing = models.ForeignKey(Listings, default=None, on_delete=models.CASCADE)
    
    # String representation of the Update model
    def __str__(self):
        return self.status
