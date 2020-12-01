from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Comment

GENDERS = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"), ("Prefer Not to Say", "Prefer Not to Say"))
TITLES = (("Mr.", "Mr."), ("Ms.", "Ms."), ("Mrs.", "Mrs."), ("Other", "Other"))
ACCOUNT_TYPES = (("Huntee", "Huntee"), ("Hunter", "Hunter"))
PRIVACY = (("Public", "Public"), ("Private", "Private"))
RATING = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))
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
  privacy = forms.ChoiceField(widget=forms.Select(), choices=PRIVACY)

  class Meta:
    model = Profile
    fields = ['profile_picture', 'resume', 'website', 'privacy']

class AddCommentForm(forms.ModelForm):
  employment = forms.CharField(max_length=150, min_length=1, strip=True)
  rating = forms.ChoiceField(widget=forms.Select(), choices=RATING)

  class Meta:
    model = Comment
    fields = ['rating', 'employment', 'comment']