from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from .validators import validate_image_file_extension

# Create your models here.


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="owner",null=True)
    title = models.CharField(default="", max_length=200, blank=True)
    time = models.DateTimeField(default=timezone.now(), blank=True)
    ispublic = models.BooleanField(default=False)
    description = models.CharField(max_length=250, default="", blank=True)

    def __str__(self):
        return self.name

    def id(self):
        return self.id


def upload_gallery_image(instance, filename):
    return f"images/{instance.gallery.owner}/{instance.gallery.name}/{filename}"


class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'gif', 'png'])])
    gallery = models.ForeignKey(
            Gallery, on_delete=models.CASCADE, related_name="images")
    created = models.DateTimeField(default=timezone.now(), blank=True)
    img_description = models.CharField(max_length=200, default="", blank=True)
    thumbnail_small = ImageSpecField(source='image',
				processors=[ResizeToFill(100,105)],
				format='JPEG',
				options={'quality':60})
    thumbnail_large= ImageSpecField(source='image',
				processors=[ResizeToFill(300,320)],
				format='JPEG',
				options={'quality':60})
