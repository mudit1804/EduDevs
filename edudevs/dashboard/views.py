# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import workform
from .models import workspaces
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect



# Create your views here.
@login_required(login_url='/$/')
def dashboard(request):
    return render(request,'dashboard/main.html')


@login_required(login_url='/$/')
def mainpanel(request):
    print "hoye"
    return render(request,'dashboard/dashboard.html')



@login_required(login_url='/$/')
def newworkspace(request):
    if request.method == 'POST':
        form = workform(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, "dashboard/dashboard.html")
            return redirect('/mainpanel/')
        else:
            print form.errors
            
    else:
        form = workform()
        
    return render(request,'dashboard/newworkspace.html')


@login_required(login_url='/$/')
def joinworkspace(request):
    return render(request,'dashboard/joinworkspace.html')


