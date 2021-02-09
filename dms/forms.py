from django import forms
from .models import Message

class NewMessageForm(forms.ModelForm):
    recipient = forms.CharField(strip=True)
    content = forms.CharField(max_length=500, min_length=0, strip=True)

    class Meta:
        model = Message
        fields = ['content']