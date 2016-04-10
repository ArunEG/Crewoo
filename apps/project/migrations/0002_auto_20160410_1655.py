# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='createdby',
            field=models.ForeignKey(to='staffs.Staff', related_name='task_createdby'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='modifiedby',
            field=models.ForeignKey(to='staffs.Staff', related_name='task_modifedby'),
        ),
        migrations.AddField(
            model_name='tasks',
            name='modules',
            field=models.ForeignKey(to='project.Modules'),
        ),
        migrations.AddField(
            model_name='project',
            name='createdby',
            field=models.ForeignKey(to='staffs.Staff', related_name='project_createdby'),
        ),
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(to='staffs.Staff'),
        ),
        migrations.AddField(
            model_name='project',
            name='modifiedby',
            field=models.ForeignKey(to='staffs.Staff', related_name='project_modifedby'),
        ),
        migrations.AddField(
            model_name='modules',
            name='createdby',
            field=models.ForeignKey(to='staffs.Staff', related_name='modules_createdby'),
        ),
        migrations.AddField(
            model_name='modules',
            name='modifiedby',
            field=models.ForeignKey(to='staffs.Staff', related_name='modules_modifedby'),
        ),
        migrations.AddField(
            model_name='modules',
            name='project',
            field=models.ForeignKey(to='project.Project'),
        ),
        migrations.AddField(
            model_name='commends',
            name='project',
            field=models.ForeignKey(to='project.Project'),
        ),
    ]
