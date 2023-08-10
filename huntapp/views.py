from django.shortcuts import render, redirect
from huntapp.models import Category
from django.contrib import messages

def home(req):
    return render(req, 'home.html')

def category(req):
    return render(req, 'category.html')

def cate_form(req):    
    if req.method=="POST":
        cid=req.POST.get('cid')
        cname=req.POST.get('cname')
        c=Category(cid=cid, cname=cname)
        print(c)
        c.save()
        messages.add_message(req, messages.SUCCESS, "Your data is successfully submit")
    data = Category.objects.all()
    print(data)
    return render(req, 'category.html' ,{'data':data})

def categorydata(req):
    data=Category.objects.all()
    return render(req, 'categorydata.html', {'data':data})

def update_data(req, id):
    if req.method=="POST":
        cid=req.POST.get('cid')
        cname=req.POST.get('cname')
        data=Category(cid=cid, cname=cname)
        data.save()
        return redirect('/categorydata/')
    else:
        data = Category.objects.get(id=id)
    return render(req, 'updatedata.html')
    
        
    

def delete_data(req, id):
    d = Category.objects.get(pk=id)
    d.delete()
    return redirect('/categorydata/')
    

        