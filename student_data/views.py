from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def form(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        enno=request.POST.get('enno')
        dob=request.POST.get('dob')

        created = student.objects.create(name=name, enno=enno, dob=dob)
        created.save()
        return redirect(st_ls)
    return render(request, 'form.html')


def st_ls(request):
    st=student.objects.all()
    context={
        "st" : st
    }
    return render(request, 'student_list.html', context)

def st_up(request,id):
    x= student.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        enno=request.POST.get('enno')
        dob=request.POST.get('dob')
        
        x.name=name
        x.enno=enno
        x.dob=dob
        x.save()
        return redirect('st_ls')
    
    return render(request, 'student_update.html', {'student' : x })

def st_del(request,id):
    x= student.objects.get(id=id)
    # if request.method == 'POST':
    x.delete()
    return redirect('st_ls')
    