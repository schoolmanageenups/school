# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import Admin_panel,Classes,Section
from teacher.models import Teachers
import random
import datetime
import time

# Create your views here.
def login(request):
   
    return render(request, 'admin/login.html',{'form' : ''})

def admin_login(request):
    if request.POST.get("login"):
      admin_login_action(request)
      return HttpResponse("login")
    # return render(request,'login.html')
    else:
      return render(request,'ajRead.html')  

def admin_login_action(request):
   
    email=request.POST.get('email','')
    password=request.POST.get('password','')
    # r=Employee.objects.all().filter(name=name,password=psw)
    r=Admin_panel.objects.all().filter(email=email,password=password)
    print (r)
    if r.exists():
        # 
        print (r[0].email)
        request.session["un"]=r[0].id
              #passing db data
        st={
         'data':r
        }
        return render(request, 'admin/panel.html', st)
       # dc={'email':email,'password':password}
       # return render(request,'dashboard.html',{'dic':dc})
        
    else:
        return render(request, 'admin/login.html', {'form' : 'invalid uname psw'})

def rdData(request):
    return render(request, 'admin/regTeacher.html',{'form' : ''})

def check(request):
    
    if request.POST.get("reg"):
      ins(request)
      #return HttpResponse("inserted")
      return render(request,'admin/panel.html')
    else:
      return render(request,'ajRead.html')  

def ins(request):
    
    name=request.POST.get('name','')
    email=request.POST.get('email','')
    password=request.POST.get('password','')  
    teacher_id=request.POST.get('teacher_id','') 
    phone=request.POST.get('phone','') 
    address=request.POST.get('address','') 
    gender=request.POST.get('gender','') 
    category=request.POST.get('category','') 
    joining=request.POST.get('joining','') 
    qualification=request.POST.get('qualification','') 

    b = Teachers(name=name,email=email,password=password,teacher_id=teacher_id,phone=phone,address=address,gender=gender,category=category,joining=joining,qualification=qualification)
    b.save()
    
    return render(request,'admin/panel.html')

def add_class(request):
   
    return render(request, 'admin/add_class.html',{'form' : ''})

def add_class_action(request):
    
    if request.POST.get("submit"):
      insert_class(request)
      #return HttpResponse("inserted")
      return render(request,'admin/panel.html')
    else:
      return render(request,'ajRead.html') 

def insert_class(request):
    
    name=request.POST.get('name','')

    b = Classes(name=name)
    b.save()
   
    return render(request,'admin/panel.html')

def add_section(request):
   
    return render(request, 'admin/add_section.html',{'form' : ''})

def add_section_action(request):
    
    if request.POST.get("submit"):
      insert_section(request)
      #return HttpResponse("inserted")
      return render(request,'admin/panel.html')
    else:
      return render(request,'ajRead.html') 

def insert_section(request):
    
    Class=request.POST.get('class','')
    section=request.POST.get('section','')

    b = Section(Class=Class,section=section)
    b.save()
   
    return render(request,'admin/panel.html')