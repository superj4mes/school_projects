from django import forms
from .models import Gallery, Image


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('name','ispublic','description')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
