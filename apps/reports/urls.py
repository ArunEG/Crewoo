'''
Created on 3/4/2016

@author: Arun Gopi
'''

from django.conf.urls import patterns, url
from apps.reports import views

urlpatterns = patterns('',

   
   url(r'^projects/$',views.projects,name='projects'),
   url(r'^new/project/$',views.new_project,name='new_project'),
   url(r'^upload/excel$',views.upload_file,name='upload_file'),
  
)