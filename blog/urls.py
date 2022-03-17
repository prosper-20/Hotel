from django.urls import path
from .views import Home

urlpatterns = [
    path("blog/", Home.as_view(), name="blog_home")
    
]