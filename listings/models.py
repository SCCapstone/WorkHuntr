import datetime

from django.db import models
from django.utils import timezone
# Create your models here.



class Listings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title, self.description


