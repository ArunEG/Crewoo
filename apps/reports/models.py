from django.db import models
from .managers import *

class ProjectInfo(models.Model):
    name = models.CharField(max_length=30,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    start_date = models.DateTimeField(null=False,blank=False)
    end_date = models.DateTimeField(null=False,blank=False)
    is_deleted = models.BooleanField(default=False)
    createdon = models.DateTimeField(auto_now_add=True)
    # createdby = models.ForeignKey(User)
    lastmodon = models.DateTimeField(auto_now=True)

    objects = ProjectInfoManager()
