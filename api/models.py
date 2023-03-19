from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return first 50 characters
        return self.body[0:50]

class User(AbstractUser):
    username = models.CharField(max_length=200, null=True,unique=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=6, null=True)
    
    def __str__(self):
        return self.username