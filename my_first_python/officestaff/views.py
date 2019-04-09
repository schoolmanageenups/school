# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from models import
from models import Ptaauthorities,Studentfees,Achievements,Examnotification,Addteacher
from datetime import datetime





def pta(request):
	return render(request,'office_staff/pta_authorities.html')
def addpta(request):
	print "as"
	name=request.POST.get('name','')
	Email=request.POST.get('email','')
	Phone=request.POST.get('Phone','')
	Occupation=request.POST.get('occupation','')
	Desig=request.POST.get('designation','')
	print "asxdx"
	a = Ptaauthorities(Name=name,Email=Email,Phone=Phone,Occupation=Occupation,Designation=Desig)
	a.save()
	return render(request,'office_staff/pta_authorities.html')

def	fees(request):
	return render(request,'office_staff/add_fees.html')
def addfees(request):
	admsn=request.POST.get('admission','')
	student=request.POST.get('student','')
	fee=request.POST.get('fees','')
	b=Studentfees(Admission_number=admsn,Student=student,Fees=fee)
	b.save()
	return render(request,'office_staff/add_fees.html')
def	achieve(request):
	return render(request,'office_staff/add_achievements.html')
def addachieve(request):
	title=request.POST.get('title','')
	discr=request.POST.get('dis','')
	image=request.POST.get('image','')
	c=Achievements(Title=title,Discription=discr,Image=image)
	c.save()	
	return render(request,'office_staff/add_achievements.html')	
def examnotif(request):
	return render(request,'office_staff/addexam_notif.html')
def addexamnotif(request):
	title=request.POST.get('title','')
	clas=request.POST.get('class','')
	Discr=request.POST.get('discription','')
	Date=request.POST.get('date','')
	d=Examnotification(Title=title,Class=clas,Discription=Discr,Date=Date)
	d.save()
	return render(request,'office_staff/addexam_notif.html')
def teach(request):
	return render(request,'office_staff/add_teacher.html')	

def teachers(request):
	name=request.POST.get('name','')
	Email=request.POST.get('email','')
	Username=request.POST.get('username','')
	Password=request.POST.get('password','')
	Phone=request.POST.get('phone','')
	Address=request.POST.get('address','')
	Gender=request.POST.get('gender','')
	mstatus=request.POST.get('status','')
	Salaryscale=request.POST.get('salary','')
	Qualification=request.POST.get('qualific','')
	Doj=request.POST.get('date','')
	Dob=request.POST.get('dob','')
	e=Addteacher(Name=name,Email=Email,Username=Username,Password=Password,Phone=Phone,Address=Address,Gender=Gender,Status=mstatus,Salaryscale=Salary,Qualification=Qualification,Doj=Date_of_joining,DOB=Dob)
	e.save()
	return render(request,'office_staff/add_teacher.html')
