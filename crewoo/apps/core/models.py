from __future__ import unicode_literals

from django.db import models

from .behaviors import Timestampable
# Create your models here.

class Team(Timestampable):

    name = models.CharField(_('Name of Team'), blank=True, max_length=255)
    users = models.ManyTomany('User', blank=True, max_length=255)

    def __str__(self):
        return self.name



class Project(Timestampable):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of Project'), blank=True, max_length=255)
    description = models.CharField(_('Description of Project'), blank=True, max_length=255)
    
    modules = models.ManyTomany('Module', blank=True, max_length=255)

    def __str__(self):
        return self.name

class Module(Timestampable):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of Module'), blank=True, max_length=255)
    tasks = models.ManyTomany('Task', blank=True, max_length=255)

    def __str__(self):
        return self.username


class Task(Timestampable):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    skills = models.ManyTomany('Skill', blank=True, max_length=255)

    def __str__(self):
        return self.username


class Skill(Timestampable):

    name = models.CharField(_('Skill of Project'), blank=True, max_length=255)

    def __str__(self):
        return self.name

