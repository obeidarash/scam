from django.urls import path
from .views import login_user, signup, log_out, profile, search, q

app_name = 'users'

urlpatterns = [
    path('login', login_user, name='login'),
    path('logout', log_out, name='logout'),
    path('signup', signup, name='signup'),
    path('profile', profile, name='profile'),
    path('search', search, name='search'),
    path('q', q, name='q'),
]
