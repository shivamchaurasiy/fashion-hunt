from django.db import models

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    contact_num=models.IntegerField()
    email=models.EmailField()
    suggestion=models.CharField(max_length=50)
    
