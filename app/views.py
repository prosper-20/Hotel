from typing import List
from django.shortcuts import render, get_object_or_404
from .models import Room, RoomImage, Staff
from django.views.generic import ListView, DetailView
from blog.models import Post


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
    extra_context={'staffs': Staff.objects.all(), 'posts': Post.objects.all()}

class RoomDetailView(DetailView):
    model = Room


def detail_view(request, slug):
    room = get_object_or_404(Room, slug=slug)
    photos = RoomImage.objects.filter(room=room)
    return render(request, 'app/room_detail.html', {
        'room':room,
        'photos':photos
    })

def contact(request):
    return render(request, "app/contact-us.html")


def about(request):
    staffs = Staff.objects.all()
    context = {"staffs": staffs}
    return render(request, "app/about-us.html", context)


def search_posts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        # This returns the results of the user's search
        rooms = Room.objects.filter(title__contains=searched)
        return render(request, "order/new_search_posts.html", {'searched': searched, 'rooms': rooms})
    else:
        return render(request, "order/new_search_posts.html")