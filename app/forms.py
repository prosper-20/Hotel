from django import forms
from .models import Category

class AvailabilityForm(forms.Form):
    room_category = forms.ChoiceField(choices=Category, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%m-%d-%YT%H:%M,"])
    check_out = forms.DateTimeField(required=True, input_formats=["%m-%d-%YT%H:%M,"])