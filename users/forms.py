#
# Forms for the Users app
#

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Code, Comment, Profile, Skill, History

# Genders for a User
GENDERS = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"), ("Prefer Not to Say", "Prefer Not to Say"))
# Titles for a User
TITLES = (("Mr.", "Mr."), ("Ms.", "Ms."), ("Mrs.", "Mrs."), ("Other", "Other"))
# Account types for a User
ACCOUNT_TYPES = (("Huntee", "Huntee"), ("Hunter", "Hunter"))
# Privacy settings for a User
PRIVACY = (("Public", "Public"), ("Private", "Private"))
# Ratings for a Comment
RATINGS = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))
# Formats for dates
DATE_FORMAT = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']

#
# Form to create a new User
#
class UserCreateAccountForm(UserCreationForm):
    title = forms.ChoiceField(widget=forms.Select(), choices=TITLES)
    first_name = forms.CharField(max_length=20, min_length=1, strip=True)
    last_name = forms.CharField(max_length=20, min_length=1, strip=True)
    gender = forms.ChoiceField(widget=forms.Select(), choices=GENDERS)
    account_type = forms.ChoiceField(widget=forms.Select(), choices=ACCOUNT_TYPES)
    email = forms.EmailField(required=True)
    birthday = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    current_employment = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['title', 'first_name', 'last_name', 'birthday', 'gender', 'current_employment', 'account_type', 'username', 'email', 'password1', 'password2']

#
# Form to input a 2FA code
#
class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code', help_text='Enter email verification code.')

    class Meta:
        model = Code
        fields = ['number']

#
# Form to update the information of a User
#
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

#
# Form to update the Profile information of a User
#
class ProfileUpdateForm(forms.ModelForm):
    privacy = forms.ChoiceField(widget=forms.Select(), choices=PRIVACY)

    class Meta:
        model = Profile
        fields = ['profile_picture', 'resume', 'website', 'privacy']

#
# Form to add a Comment to a Profile
#
class AddCommentForm(forms.ModelForm):
    rating = forms.ChoiceField(widget=forms.Select(), choices=RATINGS)
    company = forms.CharField(max_length=20, required=True, help_text='Max 20 characters')
    comment = forms.CharField(widget=forms.Textarea(), max_length=500, required=True, help_text='Max 500 characters')

    class Meta:
        model = Comment
        fields = ['rating', 'company', 'comment']

#
# Form to modify an existing Comment
#
class ModifyCommentForm(forms.ModelForm):
    rating = forms.ChoiceField(widget=forms.Select(), choices=RATINGS)
    company = forms.CharField(max_length=20, required=True, help_text='Max 20 characters')
    comment = forms.CharField(widget=forms.Textarea(), max_length=500, required=True, help_text='Max 500 characters')

    class Meta:
        model = Comment
        fields = ['rating', 'company', 'comment']

#
# Form to add a Skill to a Profile
#
class AddSkillForm(forms.ModelForm):
    skill = forms.CharField(max_length=20, required=True, help_text='Max 20 characters')

    class Meta:
        model = Skill
        fields = ['skill']

#
# Form to add a History to a Profile
#
class AddHistoryForm(forms.ModelForm):
    company = forms.CharField(max_length=20, min_length=1, strip=True, help_text='Max 20 characters')
    description = forms.CharField(widget=forms.Textarea(), max_length=500, min_length=1, strip=True, help_text='Max 500 characters')
    start_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    end_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    
    class Meta:
        model = History
        fields = ['company', 'description', 'start_date', 'end_date']

#
# Form to modify an existing History
#
class ModifyHistoryForm(forms.ModelForm):
    company = forms.CharField(max_length=20, required=True, help_text='Max 20 characters')
    description = forms.CharField(widget=forms.Textarea(), max_length=500, required=True, help_text='Max 500 characters')
    start_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    end_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    
    class Meta:
        model = History
        fields = ['company', 'description', 'start_date', 'end_date']
