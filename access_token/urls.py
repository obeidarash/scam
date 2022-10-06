from django.urls import path
from .views import at, at_generator

app_name = 'at'
urlpatterns = [
    path('a', at, name='at'),
    path('a_generator', at_generator, name='at_generator'),
]
