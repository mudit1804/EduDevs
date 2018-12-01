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


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=200)
    wname = models.CharField(blank=True, max_length=200)
    description = models.CharField(blank=True, max_length=1200)
    slug = models.CharField(max_length=150, unique=True)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name





