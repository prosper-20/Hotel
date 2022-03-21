from django import forms
from .models import Category


CATEGORY_CHOICES = (
    ("ST", "STANDARD"),
    ("KN", "KING"),
    ("EXE", "EXECUTIVE"),
    ("DX", 'DELUXE')
)

class AvailabilityForm(forms.Form):
    room_category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%m-%d-%YT%H:%M,"])
    check_out = forms.DateTimeField(required=True, input_formats=["%m-%d-%YT%H:%M,"])