from django import forms
from django.forms import ModelForm
from .models import Listings

class ListingsForm(ModelForm):
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
    
    description = forms.CharField(required=True)
    tag1 = forms.ChoiceField(choices=TAGS, required=False)
    tag2 = forms.ChoiceField(choices=TAGS, required=False)
    tag3 = forms.ChoiceField(choices=TAGS, required=False)

    class Meta:
        model = Listings
        fields = ['title', 'price', 'description', 'tag1', 'tag2', 'tag3']
        

class ModifyListingForm(forms.ModelForm):
    
    class Meta: 
        model = Listings
        fields = ['title', 'price', 'description', 'tag1', 'tag2', 'tag3', 'status']
