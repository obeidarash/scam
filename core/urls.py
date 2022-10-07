from django.urls import path
from .views import manifest, contact

# todo: add dbbackup to this app
# use this youtube tutorial https://www.youtube.com/watch?v=s54HYoJ8wrs&list=PLeg9XWX-QxbwLvK8O_xIG6zaCrON-Frjq&index=1
# add a 'get backup' button and a cronjob

app_name = 'core'

urlpatterns = [
    path('manifesto', manifest, name='manifest'),
    path('contact', contact, name='contact'),
]
