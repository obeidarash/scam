from django.urls import path
from .views import deposit

app_name = 'financial'

urlpatterns = [
    path('deposit', deposit, name='deposit'),
]
