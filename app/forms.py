import email
from logging import PlaceHolder
from django import forms
from .models import Category



class AvailabilityForm(forms.Form):
    name = forms.CharField(help_text="Enter a username")
    email = forms.EmailField(help_text="Enter a valid email address")
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])