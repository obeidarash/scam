from django.urls import path
from .views import ac, ac_generator

app_name = 'ac'
urlpatterns = [
    path('ac', ac, name='ac'),
    path('ac_generator', ac_generator, name='ac_generator'),
]
