from django.urls import path
from .views import login_user, signup, log_out

app_name = 'users'

urlpatterns = [
    path('login', login_user, name='login'),
    path('logout', log_out, name='logout'),
    path('signup', signup, name='signup'),
]
