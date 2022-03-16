from django.urls import path, include
from .views import HomeView, RoomDetailView
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("room/<slug:slug>/", RoomDetailView.as_view(), name="room_detail"),
    path('rooms/<slug:slug>/', views.detail_view, name='detail')
]
