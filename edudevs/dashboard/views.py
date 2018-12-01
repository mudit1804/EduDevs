# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import workform
from .models import workspaces
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import get_template, render_to_string
from .models import requestedmailids
from .models import requestmailform





# Create your views here.
@login_required(login_url='/$/')
def dashboard(request):
    return render(request,'dashboard/main.html')


@login_required(login_url='/$/')
def mainpanel(request, wname):
    
    print "hoye"
    return render(request,'dashboard/dashboard.html',{'wname': wname})



@login_required(login_url='/$/')
def newworkspace(request):
    curruser = request.user
    myemail = curruser.email
    if request.method == 'POST':
        form = workform(request.POST)
        if form.is_valid():
            form.save()
            # newentry = workspaces(adminmail = curruser)
            # newentry.save()
            emailids = []
            nemail = form.cleaned_data.get('nemail')
            wname = form.cleaned_data.get('wname')
            mymailentry = requestedmailids(mailid = myemail, requester=myemail, wname=wname)
            mymailentry.save()
            print nemail
            for i in range(1,int(nemail)+1):
                ename = form.cleaned_data.get('email' + str(i))
               
                if ename != "":
                    savemail = requestedmailids(mailid = ename, requester=myemail, wname=wname)
                    savemail.save()
                    emailids.append(ename)
                    #sending emails to the respective email id's
                    from_email = myemail
                    to_list = [ename]
                    c = {'wname': wname,
                          'mailid': ename,
                          'mymailid': myemail,}
                    html_content = render_to_string('dashboard/mailtemplate.html', c)
                    subject = "EduDevs: Workspace Join Request"
                    text_msg = "Request to join my workspace"
                    send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                        )

            print emailids 
            
            return HttpResponseRedirect('/dashboard/mainpanel/' + wname)
        else:
            print form.errors
            
    else:
        form = workform()
        
    return render(request,'dashboard/newworkspace.html', {'adminmail': myemail} )


@login_required(login_url='/$/')
def joinworkspace(request):
    curruser = request.user
    allworkspaces = workspaces.objects.all()
    allrequests = requestedmailids.objects.all()
    myemail = curruser.email
    loginworkspaces = []
    for prequest in allrequests:
        if prequest.mailid == myemail:
            loginworkspaces.append(prequest.wname)

    if request.method == 'POST':
        form = requestmailform(request.POST)
        if form.is_valid():
            wname = form.cleaned_data.get('wname')
            print wname
            flag = False
            for request in allrequests:
                if(request.wname == wname):
                    flag = True
                    break
            if(flag == False):
                print "workspace not exist"
                #to do
            
            flag1 = False
            for request in allrequests:
                if(request.mailid == myemail and wname == request.wname):
                    flag1 = True
                    break
            if(flag1 == True):
                #mail id hai
                print "hi mudit"
                return HttpResponseRedirect('/dashboard/mainpanel/' + wname)


            else:
                #mail id nahi hai
                
                for wp in allworkspaces:
                    if (wp.wname == wname):
                        adminmail = wp.adminmail
                
                from_email = myemail
                to_list = [adminmail]
                print adminmail
                c = {'wname': wname,
                          'adminmail': adminmail,
                          'mymail': myemail,}
                html_content = render_to_string('dashboard/mail1.html', c)
                subject = "EduDevs: Request to Join a Workspace"
                text_msg = "Request to join my workspace"
                send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                )
                return HttpResponseRedirect('/dashboard')





            


        else:
            print form.errors
    else:
        form = requestmailform()

    return render(request,'dashboard/joinworkspace.html',{'loginworkspaces':loginworkspaces})


