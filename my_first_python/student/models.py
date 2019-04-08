# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=500)
    phone=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    student_id=models.CharField(max_length=300)
    
    gender=models.CharField(max_length=300)
    dob=models.CharField(max_length=300)
    joining=models.CharField(max_length=300)
    Class=models.CharField(max_length=300)
    section=models.CharField(max_length=300)
    guardian=models.CharField(max_length=300)