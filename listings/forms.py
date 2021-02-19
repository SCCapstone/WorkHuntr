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

TYPE = [
    ('Master Card', 'Master Card'),
    ('Visa', 'Visa'),
    ('American Express', 'American Express'),
    ('Discover', 'Discover')
]

STATE = [
    ('Alabama', 'AL'),
    ('Alaska', 'AK'),
    ('Arizona', 'AZ'),
    ('Arkansas', 'AR'),
    ('California', 'CA'),
    ('Colorado', 'CO'),
    ('Connecticut', 'CT'),
    ('Delaware', 'DE'),
    ('Florida', 'FL'),
    ('Georgia', 'GA'),
    ('Hawaii', 'HI'),
    ('Idaho', 'ID'),
    ('Illinois', 'IL'),
    ('Indiana', 'IN'),
    ('Iowa', 'IA'),
    ('Kansas', 'KS'),
    ('Kentucky', 'KY'),
    ('Louisiana', 'LA'),
    ('Maine', 'ME'),
    ('Maryland', 'MD'),
    ('Massachusetts', 'MA'),
    ('Michigan', 'MI'),
    ('Minnesota', 'MN'),
    ('Mississippi', 'MS'),
    ('Missouri', 'MO'),
    ('Montana', 'MT'),
    ('Nebraska', 'NE'),
    ('Nevada', 'NV'),
    ('New Hampshire', 'NH'),
    ('New Jersey', 'NJ'),
    ('New Mexico', 'NM'),
    ('New York', 'NY'),
    ('North Carolina', 'NC'),
    ('North Dakota', 'ND'),
    ('Ohio', 'OH'),
    ('Oklahoma', 'OK'),
    ('Oregon', 'OR'),
    ('Pennsylvania', 'PA'),
    ('Rhode Island', 'RI'),
    ('South Carolina', 'SC'),
    ('South Dakota', 'SD'),
    ('Tennessee', 'TN'),
    ('Texas', 'TX'),
    ('Utah', 'UT'),
    ('Vermont', 'VT'),
    ('Virginia', 'VA'),
    ('Washington', 'WA'),
    ('West Virginia', 'WV'),
    ('Wisconsin', 'WI'),
    ('Wyoming', 'WY'),
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

class PaymentForm(forms):

    first_name = forms.CharField(max_length=20, min_length=1, strip=True, required=True)
    last_name = forms.CharField(max_length=20, min_length=1, strip=True, required=True)
    card_number = forms.IntegerField(min_length=16, max_length=16, required=True)
    type = forms.ChoiceField(widget=forms.Select(), choices=TYPE, required=True)
    exp_month = forms.IntegerField(min_length=1, max_length=2, default=1, null=False, required=True)
    exp_year = forms.IntegerField(min_length=4, max_length=4, default=2021, null=False, required=True)
    cvv = forms.IntegerField(min_length=3, max_length=3, default=123, null=False, required = True)
    street_address = forms.CharField(min_length=9, max_length = 100, default='Street Address', null=False, required=True)
    billing_city = forms.CharField(max_length=20, min_length=3, default='City', null=False, required=True)
    billing_state = forms.ChoiceField(widget=forms.Select(), choices=STATE, required=True)
    zip = forms.IntegerField(min_length=5, max_length=5, default=12345, null=False,required=True)

    class Meta:
        model = Listings
        fields = ['title', 'price']