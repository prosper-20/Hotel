from django.urls import path, include
from .views import HomeView, RoomDetailView, contact
from . import views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('room/<slug:slug>/', views.detail_view, name='detail'),
    path("contact/", views.contact, name="contact")
]
