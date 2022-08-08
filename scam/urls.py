from django.contrib import admin
from django.urls import path, include
from .views import index, manifest
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('manifest', manifest, name='manifest'),
    path('', include('users.urls', namespace='users'))
]

admin.site.site_header = "Admin Area"
admin.site.site_title = "Title"
admin.site.index_title = "Welcome to Admin Area"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
