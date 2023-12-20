from django.urls import path
from .views import login, home, profile, posts
app_name = 'web'
urlpatterns = [
    path('',login, name='login'),
    path('home', home, name='home'),
    path('profile', profile, name='profile'),
    path('posts', posts, name='posts')
]
