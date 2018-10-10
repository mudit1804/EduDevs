from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from forms import SignUpForm


import datetime

def register(request):
    if request.method == 'POST':
        print "in post"
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print "hi shrestha"
            name = form.cleaned_data.get('name')
            print name
            uemail = form.cleaned_data.get('email')
            print uemail
            username = form.cleaned_data.get('username')
            print username
            password = form.cleaned_data.get('password1')
            print password
            # repassword = form.cleaned_data('repeat-pass')
            # print repassword
            user = authenticate(username=username, password=password)
            return HttpResponseRedirect('/login')
            
            
        else:
            print form.error_messages
    else:
        print "not in post"
        form = SignUpForm()
    return render(request, 'edudevs/signup.html', {'form': form})


def mylogin(request):
    print "in login"
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
    return render(request,'edudevs/login.html')