from django.db import models

class Audition(models.Model):
    cid = models.CharField(max_length=50)
    cname=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    img=models.FileField(upload_to='audition/', default=None, null=True)
    # date=models.DateField()