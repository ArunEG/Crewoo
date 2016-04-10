from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'pm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.reports.urls')),
    url(r'^', include('apps.project.urls')),
    url(r'^', include('apps.staffs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

)