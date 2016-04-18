# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20160410_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('lastmodon', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('file', models.FileField(max_length=200, upload_to='project/attachment', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='attachments',
            field=models.ManyToManyField(to='project.ProjectAttachment'),
        ),
    ]
