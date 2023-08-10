from django.shortcuts import render, redirect
from contact.models import Contact


def contact(req):
    if req.method=="POST":
        name=req.POST['name']
        email=req.POST['email']
        phonenumber=req.POST['phonenumber']
        comment=req.POST['textarea']
        obj=Contact(name=name, email=email, phonenumber=phonenumber,comment=comment)
        obj.save()
        return redirect('/contact/')
    else:
        return render(req, 'contact.html')
        
