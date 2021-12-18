from django.contrib import admin
from .models import Gallery, Image

# Register your models here.

# StackedInline


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
