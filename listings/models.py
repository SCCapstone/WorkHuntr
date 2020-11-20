from django.db import models

# Create your models here.

class AddListings(models.model):
    listing_title = models.CharField(max_length=200)
    listing_date = models.DateTimeField('date listed')
    listing_description = models.TextField(blank=True)

    def __str__(self):
        return (self.listing_title, self.listing_date, self.listing_description)

class ModifyListings(models.Model):
    AddListings.listing_title = models.CharField(max_length=200)
    AddListings.listing_description = models.TextField(blank=True)

    def __str__(self):
        return (self.AddListings.listing_title, self.AddListings.listing_description)

class CurrentListings(models.Model):
    current_listing_title = AddListings.listing_title
    current_listing_date = AddListings.listing_date
    current_listing_description = AddListings.listing_description

    def __str__(self):
        return (self.current_listing_title, self. current_listing_date, self.current_listing_description)

