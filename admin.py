from django.contrib import admin

from dogs.models import DogImage

# Register your models here.

@admin.register(DogImage)
class DogImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'url')