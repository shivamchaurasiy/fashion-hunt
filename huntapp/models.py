from django.db import models

class Category(models.Model):
    cid=models.CharField(max_length=20)
    cname=models.CharField(max_length=50)

