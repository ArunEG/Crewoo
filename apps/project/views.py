# from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import *
from .utils import *

# from .forms import MyForm


class ProjectList(ListView):

    """
        This class return list all active projects in
        the system

        @Author : Arun Gopi
        @Date   : 10/4/2016
    """
    template_name = 'project/project_list.html'
    projects = Project.objects.active()

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {'projects': self.projects})


class ProjectDetail(DetailView):

    """
        This class return Detailed view of the project
        required project_id as parameter
        @Author : Arun Gopi
        @Date   : 10/4/2016
    """
    template_name = 'project/project_details.html'

    def get(self, request, *args, **kwargs):
        self.project = get_or_none(Project, pk=kwargs['project_id'])

        return render(request, self.template_name, {'project': self.project})


class DownloadProject(View):
    template_name = 'project/project_list.html'

    def get(self, request, *args, **kwargs):
        print('args  : ', args)
        print('kwargs  : ', kwargs)
        data = {}
        project = get_or_none(Project, pk=kwargs['project_id'])
        if kwargs['download'] == 'pdf':
            data['project'] = project
            response = get_project_as_pdf(request, data)
        elif kwargs['download'] == 'excel':
            response = get_project_as_excel(project)
        elif kwargs['download'] == 'word':
            pass
        return response

        return render(request, self.template_name, {'projects': self.projects})
