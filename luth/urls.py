from django.conf.urls import patterns, url
from luth import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'))