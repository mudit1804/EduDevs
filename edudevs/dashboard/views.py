# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import workform, workforminv
from .models import workspaces
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import get_template, render_to_string
from .models import requestedmailids
from .models import requestmailform
from .models import Room
from django.conf import settings
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant
from django.http import JsonResponse
from .models import channelform, newchannels


fake = Faker()




# Create your views here.
@login_required(login_url='/$/')
def dashboard(request):
    return render(request,'dashboard/main.html')


@login_required(login_url='/$/')
def mainpanel(request, wname):
    
    print "hoye"
    currmembers = []
    curruser = request.user
    currmail = curruser.email
    allmailids = requestedmailids.objects.all()
    allchannels = newchannels.objects.all()
    nchannels = []
    for channel in allchannels:
        if(channel.wname == wname):
            nchannels.append(channel.cname)
    print nchannels
    for mailid in allmailids:
        if(mailid.wname == wname and mailid.mailid != currmail):
            currmembers.append(mailid.mailid)


    return render(request,'dashboard/dashboard.html',{'wname': wname, 'currmembers': currmembers, 'nchannels': nchannels})

@login_required(login_url='/$/')
def channel(request,wname,slug):
    print wname
    print slug
    currmembers = []
    curruser = request.user
    currmail = curruser.email
    allchannels = newchannels.objects.all()

    nchannels = []
    for channel in allchannels:
        if(channel.wname == wname):
            nchannels.append(channel.cname)

    allmailids = requestedmailids.objects.all()
    for mailid in allmailids:
        if(mailid.wname == wname and mailid.mailid != currmail):
            currmembers.append(mailid.mailid)
    return render(request,'dashboard/channeldash.html',{'wname': wname, 'slug': slug, 'currmembers': currmembers,  'nchannels': nchannels})





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
            #create two default channels: general and informal
            slug_g = "general" + wname
            slug_i = "informal" + wname
            g_room = Room(name="General", wname=wname, description="Stop by and say hi! Everyone's welcome.", slug=slug_g)
            g_room.save()
            i_room = Room(name="Informal", wname=wname, description="Random chit chat. Best place to just chill", slug=slug_i)
            i_room.save()
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


@login_required(login_url='/$/')
def invitepeople(request, wname):
    curruser = request.user
    myemail = curruser.email
    if request.method == 'POST':
        print "in here man"
        form = workforminv(request.POST)
        if form.is_valid():
            # form.save()
            # newentry = workspaces(adminmail = curruser)
            # newentry.save()
            
            emailids = []
            nemail = form.cleaned_data.get('nemail')
            # wname = form.cleaned_data.get('wname')
            # mymailentry = requestedmailids(mailid = myemail, requester=myemail, wname=wname)
            # mymailentry.save()
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
            #create two default channels: general and informal
           
            return HttpResponseRedirect('/dashboard/mainpanel/' + wname)
        else:
            print form.errors
            
    else:
        form = workforminv()
        
    return render(request,'dashboard/invitepeople.html', {'adminmail': myemail, 'wname': wname} )
    


@login_required(login_url='/$/')
def newchannel(request, wname):
    curruser = request.user
    
    if request.method == 'POST':
        print "in here man"
        form = channelform(request.POST)
        if form.is_valid():
            form.save()
            channelname = form.cleaned_data.get('cname')
            print channelname
            slug = channelname + wname
            g_room = Room(name=channelname, wname=wname, description="Stop by and say hi! Everyone's welcome.", slug=slug)
            g_room.save()
            #create two default channels: general and informal
           
            return HttpResponseRedirect('/dashboard/mainpanel/' + wname)
        else:
            print form.errors
            
    else:
        form = channelform()
        
    return render(request,'dashboard/newchannel.html', {'wname': wname} )
    





def token(request):
    curruser = request.user
    uname = curruser.username
    identity = request.GET.get('identity', uname)
    device_id = request.GET.get('device', 'default')  # unique device ID

    account_sid = settings.TWILIO_ACCOUNT_SID
    api_key = settings.TWILIO_API_KEY
    api_secret = settings.TWILIO_API_SECRET
    chat_service_sid = settings.TWILIO_CHAT_SERVICE_SID

    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a unique endpoint ID for the device
    endpoint = "MiniSlackChat:{0}:{1}".format(identity, device_id)

    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    response = {
        'identity': identity,
        'token': token.to_jwt().decode('utf-8')
    }

    return JsonResponse(response)
