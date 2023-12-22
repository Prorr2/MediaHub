from django.urls import path
from .views import login, home, profile, crearPost, Posts, sendComment, sendMessage, people_messages, dm
app_name = 'web'
urlpatterns = [
    path('',login, name='login'),
    path('home', home, name='home'),
    path('profile', profile, name='profile'),
    path('crear-post', crearPost, name='crear-posts'),
    path('posts', Posts.as_view(), name='posts'),
    path('send-comment', sendComment, name='send-comment'),
    path('send-message', sendMessage, name='send-message'),
    path("people_messages", people_messages.as_view(), name="people_messages"),
    path("dm/<str:username>", dm.as_view(), name="dm")

]
