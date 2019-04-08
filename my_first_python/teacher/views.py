# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from models import Teachers
from student.models import Student
import random
import datetime
import time

# Create your views here.


def login_teacher(request):
   
    return render(request, 'teacher/login.html',{'form' : ''})


def login(request):
    
    if request.POST.get("login"):
      login_check(request)
      return HttpResponse("login")
    # return render(request,'login.html')
    else:
      return render(request,'ajRead.html')	

def login_check(request):
    email=request.POST.get('email','')
    password=request.POST.get('password','')
    # r=Employee.objects.all().filter(name=name,password=psw)
    r=Teachers.objects.all().filter(email=email,password=password)
    if r.exists():
        # 
        print r[0].email
        request.session["un"]=r[0].id
              #passing db data
        st={
         'data':r
        }
        return render(request, 'teacher/dashboard.html',{'id':r[0].id})
       # dc={'email':email,'password':password}
       # return render(request,'dashboard.html',{'dic':dc})
        
    else:
        return render(request, 'teacher/login.html', {'form' : 'invalid uname psw'})

def edit_teacher(request):
    ids=request.GET.get('id')
    r=Teachers.objects.all().filter(id=ids)
    if r.exists(): 
        request.session["un"]=r[0].id
              #passing db data
        st={
         'data':r
        }
        return render(request, 'teacher/editTeacher.html',st)
       # dc={'email':email,'password':password}
       # return render(request,'dashboard.html',{'dic':dc})
        
    else:
        return render(request, 'teacher/login.html', {'form' : 'invalid uname psw'})
    #return render(request, 'teacher/editTeacher.html',{'form' : ''})

def add_student(request):
    return render(request, 'teacher/add_student.html',{'form' : ''})

def register_student(request):
    
    if request.POST.get("register"):
      ins(request)
      #return HttpResponse("inserted")
      return render(request,'teacher/dashboard.html')
    else:
      return render(request,'ajRead.html') 

def ins(request):
    
    name=request.POST.get('name','')
    phone=request.POST.get('phone','')
    student_id=request.POST.get('student_id','') 
    address=request.POST.get('address','') 
    gender=request.POST.get('gender','') 
    dob=request.POST.get('dob','') 
    joining=request.POST.get('joining','') 
    Class=request.POST.get('Class','') 
    section=request.POST.get('section','') 
    guardian=request.POST.get('guardian','') 

    b = Student(name=name,student_id=student_id,phone=phone,address=address,gender=gender,dob=dob,joining=joining,Class=Class,section=section,guardian=guardian)
    b.save()
   
    return render(request,'teacher/dashboard.html')
def profile_edit(request):
    
    if request.POST.get("reg"):
      update_teacher(request)
      #return HttpResponse("inserted")
      return render(request,'teacher/dashboard.html')
    else:
      return render(request,'ajRead.html')  

def update_teacher(request):
    
    name=request.POST.get('name','')
    email=request.POST.get('email','')
    #password=request.POST.get('password','')  
    teacher_id=request.POST.get('teacher_id','') 
    phone=request.POST.get('phone','') 
    address=request.POST.get('address','') 
    gender=request.POST.get('gender','') 
    category=request.POST.get('category','') 
    joining=request.POST.get('joining','') 
    qualification=request.POST.get('qualification','') 
    t_id=request.POST.get('id','') 

    #b = Teachers(name=name,email=email,teacher_id=teacher_id,phone=phone,address=address,gender=gender,category=category,joining=joining,qualification=qualification)
    Teachers.objects.filter(id=t_id).update(name=name,email=email,teacher_id=teacher_id,phone=phone,address=address,gender=gender,category=category,joining=joining,qualification=qualification)
    #b.save()
    
    return render(request,'teacher/dashboard.html')

def view_students(request):
    return render(request, 'teacher/view_students.html',{'form' : ''})
    