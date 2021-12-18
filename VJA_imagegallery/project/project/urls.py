from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("gallery.urls")),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include("members.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
