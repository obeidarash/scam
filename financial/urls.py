from django.urls import path
from .views import deposit, withdraw

app_name = 'financial'

urlpatterns = [
    path('deposit', deposit, name='deposit'),
    path('withdraw', withdraw, name='withdraw'),
]
