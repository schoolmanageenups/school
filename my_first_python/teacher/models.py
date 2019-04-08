# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Teachers(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    teacher_id=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    address=models.CharField(max_length=300)
    gender=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    joining=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    
   