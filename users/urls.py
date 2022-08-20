from django.urls import path
from .views import login_user, signup, log_out, profile, forget_password

app_name = 'users'

urlpatterns = [
    path('login', login_user, name='login'),
    path('logout', log_out, name='logout'),
    path('signup', signup, name='signup'),
    path('profile', profile, name='profile'),
    path('forget-password', forget_password, name='forget_password'),
]
