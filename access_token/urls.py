from django.urls import path
from .views import at, at_generator

app_name = 'at'
urlpatterns = [
    path('at', at, name='at'),
    path('at_generator', at_generator, name='at_generator'),
]
