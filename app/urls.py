from django.urls import path, include
from .views import HomeView, RoomDetailView, contact, about, search_rooms, BookingList
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('room/<slug:slug>/', views.detail_view, name='detail'),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path('search/', views.search_rooms, name="search_rooms"),
    path("booking_list/", BookingList.as_view(), name="booking_list")
]
