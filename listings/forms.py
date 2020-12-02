from django import forms
from django.forms import ModelForm

from .models import Listings

class ListingsForm(ModelForm):

    class Meta:
        model = Listings
        fields = '__all__'
