from django.contrib import admin
from .models import Category, Room, RoomImage

class RoomImageAdmin(admin.StackedInline):
    model = RoomImage




admin.site.register(Category)
@admin.site.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageAdmin]

    class Meta:
        model = Room

@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    pass
