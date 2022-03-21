from django import forms
from .models import Category


CATEGORY_CHOICES = (
    ("1", "STANDARD"),
    ("2", 'DELUXE'),
    ("3", "KING"),
    ("4", "EXECUTIVE"),
    ("5", "BUSINESS"),
    ("6", "PREMIUM")
    
)

class AvailabilityForm(forms.Form):
    room_category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M,"])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M,"])