from django.urls import path
from .views import manifest

app_name = 'core'

urlpatterns = [
    path('manifest', manifest, name='manifest'),
]
