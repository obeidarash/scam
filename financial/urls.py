from django.urls import path
from .views import deposit, withdraw, balance

app_name = 'financial'

urlpatterns = [
    path('deposit', deposit, name='deposit'),
    path('withdraw', withdraw, name='withdraw'),
    path('balance', balance, name='balance'),
]
