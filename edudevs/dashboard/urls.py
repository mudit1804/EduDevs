from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^newworkspace/$', views.newworkspace, name='newworkspace'),
	url(r'^joinworkspace/$', views.joinworkspace, name='joinworkspace'),
	url(r'^mainpanel/(?P<wname>[\w\-]+)/$', views.mainpanel, name='mainpanel'),
	url(r'^token/$', views.token, name="token"),
	url(r'^mainpanel/(?P<wname>[\w\-]+)/(?P<slug>[\w\-]+)/$', views.channel, name='channel'),
	url(r'^mainpanel/invite/invitepeople/(?P<wname>[\w\-]+)/$', views.invitepeople, name='invitepeople'),
	url(r'^mainpanel/newchannel/channel/(?P<wname>[\w\-]+)/$', views.newchannel, name='newchannel'),
	url(r'^mainpanel/task/taskmanager/(?P<wname>[\w\-]+)/$', views.taskmanager, name='taskmanager'),
    url(r'^mainpanel/task/taskmanager/(?P<taskname>[\w ]+)/completed/$', views.taskcompleted, name='taskcompleted')
	




]
