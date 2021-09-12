from core.settings import STATIC_ROOT
from django.contrib import admin
from django.urls import path
from shop.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('admin/', admin.site.urls), path('', index, name='index')]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
