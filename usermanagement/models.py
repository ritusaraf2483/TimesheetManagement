from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user=models.OneToOneField(User,models.CASCADE)
    phone=models.CharField(max_length=13,blank=True)
    address=models.CharField(max_length=30,blank=True)
    image=models.ImageField(upload_to='images/users')