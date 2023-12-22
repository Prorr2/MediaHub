from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    alias = models.CharField(max_length = 50, default = "")
    icon = models.ImageField(upload_to="icons")
    description = models.TextField(max_length = 2000)
class UserPost(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    media = models.FileField(upload_to="posts")
    description = models.CharField(max_length = 1000)
class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete = models.CASCADE)
    content = models.CharField(max_length = 2000)
    id = models.AutoField(primary_key=True) 
class Message(models.Model):
    profile_from = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = "profile_from")
    profile_to = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = "profile_to")
    content = models.CharField(max_length = 2000)
    datetime = models.DateField(auto_now_add=True)

