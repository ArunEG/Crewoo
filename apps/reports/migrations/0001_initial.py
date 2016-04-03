# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('lastmodon', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
