from django.urls import path
from .views import manifest
app_name = 'users'

urlpatterns = [
    path('', manifest, name='manifest'),
]
