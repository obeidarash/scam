from django.urls import path
from .views import manifest, contact

app_name = 'core'

urlpatterns = [
    path('manifest', manifest, name='manifest'),
    path('contact', contact, name='contact'),
]
