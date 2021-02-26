from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': ("This account is inactive."),
    }
