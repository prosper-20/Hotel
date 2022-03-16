from typing import List
from django.shortcuts import render, get_object_or_404
from .models import Room, RoomImage
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


def detail_view(request, slug):
    room = get_object_or_404(Room, slug=slug)
    photos = RoomImage.objects.filter(post=post)
    return render(request, 'room_detail_1.html', {
        'room':room,
        'photos':photos
    })
