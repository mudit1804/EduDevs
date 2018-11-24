# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/$/')
def dashboard(request):
    return render(request,'dashboard/main.html')

@login_required(login_url='/$/')
def newworkspace(request):
    return render(request,'dashboard/newworkspace.html')


@login_required(login_url='/$/')
def joinworkspace(request):
    return render(request,'dashboard/joinworkspace.html')
