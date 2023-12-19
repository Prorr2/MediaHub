from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    icon = models.ImageField(upload_to="icons")
    description = models.TextField(max_length = 2000)