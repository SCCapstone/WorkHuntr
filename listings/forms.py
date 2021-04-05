from django import forms
from django.forms import ModelForm
from .models import Listings
from django.contrib.postgres.fields import ArrayField
from .models import Update

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

UPDATESTATUSES = [
    ('Started', 'Started'),
    ('Milestone 1', 'Milestone 1'),
    ('Milestone 2', 'Milestone 2'),
    ('Milestone 3', 'Milestone 3'),
    ('Complete', 'Complete')
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
    number_Of_Milestones = forms.CharField(required=True)

    class Meta:
        model = Listings
        fields = ['title', 'price', 'description', 'tag1', 'tag2', 'tag3', 'number_Of_Milestones']  

class ModifyListingForm(forms.ModelForm):

    tag1 = forms.ChoiceField(widget=forms.Select(), choices=TAGS, required=False)
    tag2 = forms.ChoiceField(choices=TAGS, required=False)
    tag3 = forms.ChoiceField(choices=TAGS, required=False)
    milestones = forms.CharField(help_text="Enter Milestone Names seperated by a comma")

    class Meta: 
        model = Listings
        fields = ['title', 'price', 'description', 'tag1', 'tag2', 'tag3', 'milestones']

class PaymentForm(forms.Form):
    first_name = forms.CharField(max_length=20, min_length=1, strip=True, required=True, help_text="First Name Listed on Credit Card")
    last_name = forms.CharField(max_length=20, min_length=1, strip=True, required=True, help_text="Last Name Listed on Credit Card")
    card_number = forms.IntegerField(min_value=1000000000000000, max_value=9999999999999999, required=True, help_text="16-digit Credit Card Number without Dashes")
    type = forms.ChoiceField(widget=forms.Select(), choices=TYPE, required=True, help_text="Credit Card Type")
    exp_month = forms.IntegerField(min_value=1, max_value=12, required=True, help_text="Expiration Month Ranging From 1 to 12")
    exp_year = forms.IntegerField(min_value=2021, max_value=2031, required=True, help_text="Expiration Year")
    cvv = forms.IntegerField(min_value=100, max_value=999, required = True, help_text="3-digit Number on the Back of the Card")
    street_address = forms.CharField(min_length=9, max_length = 100, required=True, help_text="Billing Street Address")
    billing_city = forms.CharField(max_length=20, min_length=3, required=True, help_text="City Containing Billing Street Address")
    billing_state = forms.ChoiceField(widget=forms.Select(), choices=STATE, required=True, help_text="State Containing Billing Street Address")
    zip = forms.IntegerField(min_value=501, max_value=99999, required=True, help_text="Zip Code of Billing Address")
    
class UpdateForm(forms.ModelForm):
    # status = forms.ChoiceField(choices=Listings.milestones, required=True)
    description = forms.CharField(required=True)
    # currentMilestone = forms.CharField(required=True)

    class Meta:
        model = Update
        fields = ['description']

class MyListingsForm(forms.Form):
    Listings = forms.ModelChoiceField(queryset=Listings.objects.values_list("title", flat=True).distinct(), empty_label=None)