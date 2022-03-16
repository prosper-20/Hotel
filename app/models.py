from django.db import models


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


    def __str__(self):
        return f"{self.number} - {self.category}"

