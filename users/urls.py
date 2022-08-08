from django.urls import path
from .views import login_user, signup

app_name = 'users'

urlpatterns = [
    path('login', login_user, name='login'),
    path('signup', signup, name='signup'),
]
