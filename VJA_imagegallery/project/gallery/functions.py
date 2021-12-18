from datetime import datetime
from .models import Image, Gallery

def time():
    current_time = datetime.now()
    date_time = current_time.strftime("%d/%m/%Y %H:%M:%S")
    return date_time

def galleryimagepairs(galleries, images):
    galleryimages = {}
    for gal in galleries:
        galleryimages[gal] = []
        for img in images:
            if(img.gallery.id == gal.id):
                galleryimages[gal].append(img)
    return galleryimages
