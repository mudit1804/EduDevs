# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


# Create your models here.
class workspaces(models.Model):
    id = models.AutoField(primary_key=True)
    wname = models.CharField(blank=False, max_length=200, unique=True)
    nemail = models.CharField(blank=True, max_length=200)
    email1 = models.CharField(blank=True, max_length=200)
    email2 = models.CharField(blank=True, max_length=200)
    email3 = models.CharField(blank=True, max_length=200)
    email4 = models.CharField(blank=True, max_length=200)
    email5 = models.CharField(blank=True, max_length=200)
    
    def __str__(self):
          return self.wname

class workform(ModelForm):
    class Meta:
        model = workspaces
        fields = ['wname','nemail','email1','email2','email3','email4','email5']


