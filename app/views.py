from django.shortcuts import render
from .models import Room


def home(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, "app/home.html", context)
