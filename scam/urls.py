from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf import settings
from django.conf.urls.static import static

# todo: Add Recaptcha to admin login page
urlpatterns = [
    path('thisispanelarea/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', index, name='home'),
    path('', include('users.urls', namespace='users')),
    path('', include('core.urls', namespace='core')),
    path('', include('financial.urls', namespace='financial')),
    path('', include('access_token.urls', namespace='ac'))
]

admin.site.site_header = "Admin Area"
admin.site.site_title = "Short Invest in Coin Technology"
admin.site.index_title = "Welcome to Short Invest in Coin Technology"
