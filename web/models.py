from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    alias = models.CharField(max_length = 50, default = "")
    icon = models.ImageField(upload_to="icons")
    description = models.TextField(max_length = 2000)
class UserPost(models.Model):
    profile = models.OneToOneField(Profile, on_delete = models.CASCADE)
    media = models.FileField(upload_to="posts")
    description = models.CharField(max_length = 1000)