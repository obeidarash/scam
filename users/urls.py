from django.urls import path
from .views import login_user, signup, log_out, profile, forget_password
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import reverse_lazy

app_name = 'users'

urlpatterns = [
    path('login', login_user, name='login'),
    path('logout', log_out, name='logout'),
    path('signup', signup, name='signup'),
    path('profile', profile, name='profile'),
    path('forget-password', forget_password, name='forget_password'),

    # Forget password urls
    path('password_reset/', PasswordResetView.as_view(template_name='users/reset_password.html',
                                                      email_template_name='users/email_template.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/reset_password_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/reset_password_confirm.html'),
         name='password_reset_confirm'),
]
