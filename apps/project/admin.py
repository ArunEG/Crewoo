from django.contrib import admin
from apps.project.models import Project, Modules, Tasks, ProjectAttachment
admin.site.register(Project)
admin.site.register(Modules)
admin.site.register(Tasks)
admin.site.register(ProjectAttachment)

