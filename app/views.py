from typing import List
from django.shortcuts import render, get_object_or_404
from .models import Room, RoomImage, Staff
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
    extra_context={'staffs': Staff.objects.all()}

class RoomDetailView(DetailView):
    model = Room


def detail_view(request, slug):
    room = get_object_or_404(Room, slug=slug)
    photos = RoomImage.objects.filter(room=room)
    return render(request, 'app/room_detail.html', {
        'room':room,
        'photos':photos
    })
