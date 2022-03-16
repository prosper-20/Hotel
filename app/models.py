from django.db import models
from django.utils.text import slugify
from django.urls import reverse


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
    image = models.ImageField()
    price = models.IntegerField()
    slug = models.SlugField()


    def __str__(self):
        return f"{self.number} - {self.category}"

    def get_absolute_url(self):
        return reverse("room_detail", kwargs={
            'slug': self.slug
        })


    def save(self, *args, **kwargs): # < here
        self.slug = slugify(self.title)
        super(Room, self).save()

