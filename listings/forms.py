from django import forms
from django.forms import ModelForm
from .models import Listings
from .models import Update

TAGS = [
    ('None', 'None'),
    ('AI', 'AI'),
    ('Development', 'Development'),
    ('Design', 'Design'), 
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('Python', 'Python'),
    ('Web', 'Web')
]

TYPES = [
    ('Master Card', 'Master Card'),
    ('Visa', 'Visa'),
    ('American Express', 'American Express'),
    ('Discover', 'Discover')
]

UPDATE_STATUSES = [
    ('Started', 'Started'),
    ('Milestone 1', 'Milestone 1'),
    ('Milestone 2', 'Milestone 2'),
    ('Milestone 3', 'Milestone 3'),
    ('Complete', 'Complete')
]

STATES = [
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
    title = forms.CharField(max_length=50, required=True, help_text='Max 20 characters')
    price = forms.DecimalField(min_value=0.00, max_value=999.99, max_digits=5, decimal_places=2, required=True)
    description = forms.CharField(widget=forms.Textarea(), max_length=1000, required=True, help_text='Max 500 characters')
    tag_one = forms.ChoiceField(widget=forms.Select(), choices=TAGS, required=False)
    tag_two = forms.ChoiceField(widget=forms.Select(), choices=TAGS, required=False)
    tag_three = forms.ChoiceField(widget=forms.Select(), choices=TAGS, required=False)

    class Meta:
        model = Listings
        fields = ['title', 'price', 'description', 'tag_one', 'tag_two', 'tag_three']  

class ModifyListingForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, help_text='Max 20 characters')
    price = forms.DecimalField(min_value=0.00, max_value=999.99, max_digits=5, decimal_places=2, required=True)
    description = forms.CharField(widget=forms.Textarea(), max_length=1000, required=True, help_text='Max 500 characters')
    tag_one = forms.ChoiceField(widget=forms.Select(), choices=TAGS, required=False)
    tag_two = forms.ChoiceField(widget=forms.Select(), choices=TAGS, required=False)
    tag_threee = forms.ChoiceField(widget=forms.Select(), choices=TAGS, required=False)

    class Meta: 
        model = Listings
        fields = ['title', 'price', 'description', 'tag_one', 'tag_two', 'tag_three']

class PaymentForm(forms.Form):
    first_name = forms.CharField(max_length=20, min_length=1, strip=True, required=True, help_text="First name listed on credit card")
    last_name = forms.CharField(max_length=20, min_length=1, strip=True, required=True, help_text="Last name listed on credit card")
    card_number = forms.IntegerField(min_value=1000000000000000, max_value=9999999999999999, required=True, help_text="16-digit credit card Number without dashes")
    type = forms.ChoiceField(widget=forms.Select(), choices=TYPES, required=True, help_text="Credit card type")
    exp_month = forms.IntegerField(min_value=1, max_value=12, required=True, help_text="Expiration month ranging from 1 to 12")
    exp_year = forms.IntegerField(min_value=2021, max_value=2031, required=True, help_text="Expiration year")
    cvv = forms.IntegerField(min_value=100, max_value=999, required = True, help_text="3-digit number on the back of the card")
    street_address = forms.CharField(min_length=9, max_length = 100, required=True, help_text="Street of billing address")
    billing_city = forms.CharField(max_length=20, min_length=3, required=True, help_text="City of billing address")
    billing_state = forms.ChoiceField(widget=forms.Select(), choices=STATES, required=True, help_text="State of billing address")
    zip = forms.IntegerField(min_value=501, max_value=99999, required=True, help_text="Zip code of billing address")
    
class UpdateForm(forms.ModelForm):
    status = forms.ChoiceField(choices = UPDATE_STATUSES, required=True)
    description = forms.CharField(widget=forms.Textarea(), max_length=500, required=True, help_text='Max 500 characters')

    class Meta:
        model = Update
        fields = ['status','description']

class MyListingsForm(forms.Form):
    Listings = forms.ModelChoiceField(queryset=Listings.objects.values_list("title", flat=True).distinct(), empty_label=None)
