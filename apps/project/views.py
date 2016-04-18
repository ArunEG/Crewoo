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
    projects = Project.objects.all()

    def get(self, request, *args, **kwargs):
        print("self.projects  : ", self.projects)
        return render(request, self.template_name, {'projects': self.projects})


class ProjectDetail(DetailView):

    """
        This class return Detailed view of the project
        required project_id as parameter
        @Author : Arun Gopi
        @Date   : 10/4/2016
    """

    template_name = 'project/project_details.html'
    attachment = None
    return_data = {}

    def dispatch(self, request, *args, **kwargs):
        """
            The function will exicute if any request is received
            It will act as a constructor for our class
        """
        self.project = get_or_none(Project, pk=kwargs['project_id'])
        self.comments = self.project.comments.all()
        attachments = self.project.attachments.all()
        if attachments:
            self.attachment = attachments[0]
        self.return_data['project'] = self.project
        self.return_data['attachment'] = self.attachment
        self.return_data['comments'] = self.comments
        return super(ProjectDetail, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.return_data)

    def post(self, request, *args, **kwargs):
        data = {}
        subject = request.POST.get('subject')
        description = request.POST.get('comment')
        data['project_id'] = self.project.pk
        data['subject'] = subject
        data['description'] = description
        save_comment(data)
        return render(request, self.template_name, self.return_data)


class DownloadProject(View):

    """
        This class will helps to download project details
        as word,pdf or excel
        required project_id as parameter
        and which format is required
        @Author : Arun Gopi
        @Date   : 10/4/2016
    """

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
            response = get_project_as_word(project)
        return response

        return render(request, self.template_name, {'projects': self.projects})
