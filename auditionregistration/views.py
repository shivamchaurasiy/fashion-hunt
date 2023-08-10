# from django.shortcuts import render, redirect
# from auditionregistration.forms import AuditionRegistrationForm
# from auditionregistration.models import AuditionRegistrationModel
# import os

# def auditionregi(req):
#     fm = AuditionRegistrationForm()
#     return render(req, 'auditionregi.html', {'form':fm})
    
# def auditionregi_data(req):
#     if req.method=="POST":
#         fm = AuditionRegistrationForm(req.POST, req.FILES)
#         if fm.is_valid():
#             fm.save()
       
#     else:
#         fm = AuditionRegistrationForm
#     d = AuditionRegistrationModel.objects.all()
#     return render(req, 'auditionregidata.html', {"data":d})

# def updateregi(req, id):
#     d = AuditionRegistrationModel.objects.get(id=id)
#     return render(req, 'updateregi.html', {'id':d})

# def updateregi_data(req, id):
#     if req.method=="POST":
#         d = AuditionRegistrationModel.objects.get(id=id)
#         nm=req.POST.get('nm')
#         place=req. POST.get('place')
#         dt=req.POST.get('dt')
#         img=req.POST.get('img')
#         data=AuditionRegistrationModel(name=nm, place=place, date=dt, img=img)
#         data.save()
#         return redirect('/auditionregidata/')

# def deleteregi_data(req, id):
#     id = AuditionRegistrationModel.objects.get(id=id)
#     id.delete()
#     return redirect('/auditionregidata/') 









from django.shortcuts import render, redirect
from .models import StudentModel
from django.core.paginator import Paginator
import os

def auditionregi(req):
    return render(req, 'auditionregi.html')


def auditionregi_data(req):
    if req.method=="POST":
        c=req.POST.get('tcid')
        n=req.POST.get('tname')
        if (len(req.FILES)!=0):
            url=req.FILES['fimg']
        data = StudentModel(cid=c, name=n, nimg=url)
        data.save()
        return redirect('/auditionregidata/')
    d = StudentModel.objects.all()
    print(d)
    p = Paginator(d, 2)
    pgno = req.GET.get('page')
    fpage = p.get_page(pgno)
    return render(req, 'auditionregidata.html', {'data':d, 'fpage':fpage})

def deleteregi_data(req, id):
    id = StudentModel.objects.get(id=id)
    id.delete()
    return redirect('/auditionregidata/')

def updateregi(req, id):
    id=StudentModel.objects.get(id=id)
    return render(req, 'updatedata.html', {'id':id})

def updateregi_data(req, id):
    d = StudentModel.objects.get(id=id)
    if req.method=='POST':
        cid=req.POST.get('tcid')
        nm=req.POST.get('tname')
        if (len(req.FILES)!=0):
            if(len(d.nimg)>0):
                os.remove(d.nimg.path)
            url=req.FILES['fimg']
        else:
            url = d.nimg
        d.cid=cid
        d.name=nm
        d.nimg=url
        d.save()
    return redirect('/auditionregidata/')
        
        
