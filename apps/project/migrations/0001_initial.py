# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('lastmodon', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=300)),
                ('detailed_description', models.TextField()),
                ('createdby', models.ForeignKey(related_name='modules_createdby', to=settings.AUTH_USER_MODEL)),
                ('modifiedby', models.ForeignKey(related_name='modules_modifedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('lastmodon', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=300)),
                ('detailed_description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('client_name', models.CharField(max_length=30)),
                ('createdby', models.ForeignKey(related_name='project_createdby', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('modifiedby', models.ForeignKey(related_name='project_modifedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('lastmodon', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=30)),
                ('short_description', models.CharField(max_length=300)),
                ('detailed_description', models.TextField()),
                ('createdby', models.ForeignKey(related_name='task_createdby', to=settings.AUTH_USER_MODEL)),
                ('modifiedby', models.ForeignKey(related_name='task_modifedby', to=settings.AUTH_USER_MODEL)),
                ('modules', models.ForeignKey(to='project.Modules')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.AddField(
            model_name='modules',
            name='project',
            field=models.ForeignKey(to='project.Project'),
        ),
    ]
