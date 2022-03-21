from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Enter a unique name.")

    def __str__(self):
        return self.name 


class Room(models.Model):
    number = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    beds = models.IntegerField()
    capacity = models.IntegerField()
    image = models.FileField(blank=True)
    price = models.IntegerField()
    slug = models.SlugField()


    def __str__(self):
        return f"{self.number} - {self.category}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })


    def save(self, *args, **kwargs): # < here
        self.slug = slugify(self.category)
        super(Room, self).save()


class RoomImage(models.Model):
    room = models.ForeignKey(Room, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.room.description

class Staff(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return f"{self.name} - {self.job}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()


    def __str__(self):
        return f"{self.user} - {self.room} from {self.check_in} to {self.check_out}"

        