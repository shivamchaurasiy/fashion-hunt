from django.shortcuts import render
from audition.models import Audition

def audition(req):
    d = Audition.objects.all()
    return render(req, 'audition.html', {'data':d})
