import email
from logging import PlaceHolder
from django import forms
from .models import Category



class AvailabilityForm(forms.Form):
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M,"])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M,"])