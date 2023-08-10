# from django.db import models

# class AuditionRegistrationModel(models.Model):
#     name=models.CharField(max_length=50)
#     place=models.CharField(max_length=50)
#     date=models.DateField()
#     regimg=models.FileField(upload_to='auditionregi/', default=None, null=True)
    

from django.db import models

class StudentModel(models.Model):
    cid=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    nimg=models.FileField(upload_to='', max_length=255, null=True, default=None)
