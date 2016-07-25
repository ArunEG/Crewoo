# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    
 url(
        regex=r'^$',
        view=TemplateView.as_view(template_name='admin/index.html'),
        name='home_page'
    ),

]

