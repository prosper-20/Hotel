from typing import List
from django.shortcuts import render
from .models import Room
from django.views.generic import ListView, DetailView


# def home(request):
#     rooms = Room.objects.all()
#     context = {
#         "rooms": rooms
#     }
#     return render(request, "app/home.html", context)


class HomeView(ListView):
    model = Room
    template_name = 'app/home.html'
    context_object_name = "rooms"

class RoomDetailView(DetailView):
    model = Room
