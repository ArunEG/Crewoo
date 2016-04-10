'''
Created on 3/4/2016

@author: Arun Gopi
'''

from django.conf.urls import patterns, url
from apps.project import views

urlpatterns = patterns('',

						url(r'^$', views.ProjectList.as_view(),
							name='projects'),
						url(r'^project/details/(?P<project_id>[0-9]+)/$', views.ProjectDetail.as_view(),
							name='project_detail'),
						url(r'^pdf/project/(?P<project_id>[0-9]+)/(?P<download>[\w-]+)/$',views.DownloadProject.as_view(),name='download_project'),
					    )
