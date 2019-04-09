# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Login(models.Model):
	Username=models.CharField(max_length=30)
	Password=models.CharField(max_length=30)
class Studentfees(models.Model):
	Admission_number=models.CharField(max_length=30)
	Student=models.CharField(max_length=30)
	Fees=models.CharField(max_length=30)
class Addteacher(models.Model):
	Name=models.CharField(max_length=30)
	Email=models.CharField(max_length=30)
	Username =models.CharField(max_length=30)
	Password=models.CharField(max_length=30)
	Teacher_id=models.CharField(max_length=30)
	Phone=models.CharField(max_length=30)
	Address=models.CharField(max_length=30)
	Gender=models.CharField(max_length=30)
	Status=models.CharField(max_length=30)
	Salary=models.CharField(max_length=30)
	Qualification=models.CharField(max_length=30)
	Date_of_joining=models.CharField(max_length=30)
	DOB=models.CharField(max_length=30)	
class Examnotification(models.Model):
	Title=models.CharField(max_length=30)
	Class=models.CharField(max_length=30)
	Discription=models.CharField(max_length=30)
	Date=models.CharField(max_length=30)
class Ptaauthorities(models.Model):
	Name=models.CharField(max_length=30)
	Email=models.CharField(max_length=30)
	Phone=models.CharField(max_length=30)
	Occupation=models.CharField(max_length=30)
	Designation=models.CharField(max_length=30)	
class Achievements(models.Model):
	Title=models.CharField(max_length=30)
	Discription=models.CharField(max_length=30)
	Image=models.ImageField(upload_to = 'pictures')		