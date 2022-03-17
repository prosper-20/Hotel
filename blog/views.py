from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class Home(ListView):
    model = Post
    context_object_name = 'posts'

