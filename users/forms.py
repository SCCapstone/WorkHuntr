from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

GENDERS = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"), ("Prefer Not to Say", "Prefer Not to Say"))
TITLES = (("Mr.", "Mr."), ("Ms.", "Ms."), ("Mrs.", "Mrs."), ("Other", "Other"))
ACCOUNT_TYPES = (("Huntee", "Huntee"), ("Hunter", "Hunter"))

class UserCreateAccountForm(UserCreationForm):
  title = forms.ChoiceField(widget=forms.Select(), choices=TITLES)
  first_name = forms.CharField(max_length=20, min_length=1, strip=True)
  last_name = forms.CharField(max_length=20, min_length=1, strip=True)
  gender = forms.ChoiceField(widget=forms.Select(), choices=GENDERS)
  account_type = forms.ChoiceField(widget=forms.Select(), choices=ACCOUNT_TYPES)
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ['title', 'first_name', 'last_name', 'gender', 'account_type', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField(required=True)
  
  class Meta:
    model = User
    fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_picture']
