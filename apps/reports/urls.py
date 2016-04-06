'''
Created on 3/4/2016

@author: Arun Gopi
'''

from django.conf.urls import patterns, url
from apps.reports import views

urlpatterns = patterns('',

   url(r'^pdf/project-info/(?P<project_id>[0-9]+)/(?P<download>[\w-]+)/$',views.projects,name='pdf_project_info'),
   url(r'^projects/$',views.projects,name='projects'),
   url(r'^upload/excel$',views.upload_file,name='upload_file'),
  
)