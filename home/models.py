from pyexpat import model
from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField( primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) -> str:
        return 'Message from ' + self.name + ' - ' + self.email

class user_token(models.Model):
    token = models.CharField(max_length=1000, unique=True)
    subscribe = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.token