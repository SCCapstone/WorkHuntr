from django import forms
from django.forms import ModelForm
from .models import Listings

class ListingsForm(ModelForm):

    class Meta:
        model = Listings
        fields = ['title', 'price', 'description', 'tag1', 'tag2', 'tag3', 'status']

class ModifyListingForm(forms.ModelForm):
    
    class Meta: 
        model = Listings
        fields = ['title', 'price', 'description', 'tag1', 'tag2', 'tag3', 'status']
