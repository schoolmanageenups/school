# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Admin_panel(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Classes(models.Model):
    name=models.CharField(max_length=50)

class Section(models.Model):
    Class=models.CharField(max_length=50)
    section=models.CharField(max_length=50)
    
    