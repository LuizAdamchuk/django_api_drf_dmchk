from email.policy import default
from django import forms

class PokeForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100, required=False)