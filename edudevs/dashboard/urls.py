from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^newworkspace/$', views.newworkspace, name='newworkspace'),
	url(r'^joinworkspace/$', views.joinworkspace, name='joinworkspace'),

]