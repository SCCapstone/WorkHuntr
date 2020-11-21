from django import forms
from django.forms import ModelForm

from .models import *

class ListingsForm(forms.ModelForm):

    class Meta:
        model = Listings
        fields = Listings.title, Listings.description
