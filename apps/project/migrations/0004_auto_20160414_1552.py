# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20160414_0513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(to='project.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='commends',
            name='project',
        ),
        migrations.DeleteModel(
            name='Commends',
        ),
    ]
