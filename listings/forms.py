from django import forms
from django.forms import ModelForm
from .models import Listings

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

class ListingsForm(ModelForm):
    
    description = forms.CharField(required=True)
    tag1 = forms.ChoiceField(widget=forms.Select(), choices=TAGS, required=False)
    tag2 = forms.ChoiceField(choices=TAGS, required=False)
    tag3 = forms.ChoiceField(choices=TAGS, required=False)

    class Meta:
        model = Listings
        fields = ['title', 'price', 'description', 'tag1', 'tag2', 'tag3']
        

class ModifyListingForm(forms.ModelForm):

    tag1 = forms.ChoiceField(widget=forms.Select(), choices=TAGS, required=False)
    tag2 = forms.ChoiceField(choices=TAGS, required=False)
    tag3 = forms.ChoiceField(choices=TAGS, required=False)

    class Meta: 
        model = Listings
        fields = ['title', 'price', 'description', 'tag1', 'tag2', 'tag3']
