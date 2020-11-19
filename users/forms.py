from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female'),
  ('Other', 'Other'),
  ('Prefer not to say', 'Prefer not to say'),
]
TITLES = [
  ('Mr.', 'Mr.'),
  ('Ms.', 'Ms.'),
  ('Mrs.', 'Mrs.'),
  ('None', 'None'),
]
ACCOUNT_TYPE = [
  (True, 'Hunter'),
  (False, 'Huntee')
]

class UserCreateAccountForm(UserCreationForm):
  email = forms.EmailField(required=True)
  title = forms.ChoiceField(required=False, widget=forms.Select(), choices=TITLES)
  gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER_CHOICES)
  first_name = forms.CharField(required=True)
  last_name = forms.CharField(required=True)
  account_type = forms.ChoiceField(required=True, widget=forms.Select(), choices=ACCOUNT_TYPE)

  
  class Meta:
    model = User
    fields = ['title', 'first_name', 'last_name', 'gender', 'username', 'account_type', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField(required=True)
  gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER_CHOICES)

  class Meta:
    model = User
    fields = ['username', 'email', 'gender']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_picture']
