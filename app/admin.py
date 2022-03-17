from django.contrib import admin
from .models import Category, Room, RoomImage, Staff

admin.site.register(Category)
admin.site.register(Staff)

class RoomImageAdmin(admin.StackedInline):
    model = RoomImage



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageAdmin]

    class Meta:
        model = Room

@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    pass
