from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    phonenumber=models.CharField(max_length=30)
    comment=models.TextField()
