from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user=models.OneToOneField(User,models.CASCADE)
    doc_id=models.CharField(max_length=15,unique=True)
    phone=models.CharField(max_length=13,blank=True)
    address=models.CharField(max_length=30,blank=True)
    image=models.ImageField(upload_to='images/users')

    def __str__(self):
        return self.doc_id
