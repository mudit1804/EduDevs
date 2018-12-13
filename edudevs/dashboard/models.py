# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


# Create your models here.
class workspaces(models.Model):
    id = models.AutoField(primary_key=True)
    wname = models.CharField(blank=False, max_length=200, unique=True)
    adminmail = models.CharField(blank=True, max_length=200)
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
        fields = ['wname','adminmail','nemail','email1','email2','email3','email4','email5']

class workforminv(ModelForm):
    class Meta:
        model = workspaces
        fields = ['adminmail','nemail','email1','email2','email3','email4','email5']

class newchannels(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(blank=True, max_length=200)
    wname = models.CharField(blank=True, max_length=200)

    

class channelform(ModelForm):
    class Meta:
        model = newchannels
        fields = ['cname','wname']
    

class requestedmailids(models.Model):
    id = models.AutoField(primary_key=True)
    mailid = models.CharField(blank=True, max_length=200)
    requester = models.CharField(blank=True, max_length=200)
    wname = models.CharField(blank=True, max_length=200)

    def __str__(self):
          return self.wname

class requestmailform(ModelForm):
    class Meta:
        model = requestedmailids
        fields = ['wname']


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    taskname = models.CharField(blank=False, max_length=200, unique=True)
    disc =  models.CharField(blank=True, max_length=5000)
    deadline = models.DateField(blank=True)
    wname = models.CharField(blank=False, max_length=200)
    adminmail = models.CharField(blank=True, max_length=200)
    nemail = models.CharField(blank=True, max_length=200)
    email1 = models.CharField(blank=True, max_length=200)
    email2 = models.CharField(blank=True, max_length=200)
    email3 = models.CharField(blank=True, max_length=200)
    email4 = models.CharField(blank=True, max_length=200)
    email5 = models.CharField(blank=True, max_length=200)
    status = models.CharField(default='Pending', max_length=100)

class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ['taskname','disc','deadline','nemail','email1','email2','email3','email4','email5','wname','adminmail']


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=200)
    wname = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=1200)
    slug = models.CharField(max_length=150, unique=True)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name





