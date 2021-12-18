from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('add_gallery.html', views.add_gallery_view, name="add_gallery"),
    path('gallery/<int:pk>/', views.gallery_view, name="gallery"),
    path('gallery/gallery_image_administration/<int:pk>/deleteimage/', views.deleteimage, name="deleteimage"),
    path('gallery/gallery_image_administration/<int:pkgal>/deleteimage/<int:pkimg>', views.deleteimage, name="deleteimage"),
    path('gallery/<int:pk>/remove', views.DeleteGalleryView.as_view(), name='delete_gallery'),
    path('gallery/gallery_image_administration/<int:pk>/', views.gallery_image_administration_view, name='gallery_image_adaministration'),
    path('gallery_administration', views.gallery_administration_view, name='gallery_administration'),
    path('gallery/<int:pk>/add', views.addPhoto, name='add_images'),
    path('gallery/<int:pk>/update', views.UpdateGalleryView.as_view(), name="update_gallery"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
