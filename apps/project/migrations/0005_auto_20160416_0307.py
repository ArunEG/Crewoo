# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20160414_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='project',
            field=models.ForeignKey(to='project.Project', related_name='comments'),
        ),
    ]
