# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, parent_link=True, to=settings.AUTH_USER_MODEL, auto_created=True, primary_key=True)),
                ('gender', models.CharField(verbose_name='Gender', max_length=1, choices=[('F', 'Female'), ('M', 'Male')])),
                ('image', models.ImageField(verbose_name='Image', null=True, upload_to='Staffs/TeamLead/', blank=True)),
                ('mobile', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.TextField(verbose_name='Address', blank=True, null=True)),
                ('dob', models.DateField(verbose_name='DOB', blank=True, null=True)),
                ('user_type', models.CharField(max_length=2, default='OT', choices=[('TL', 'Team Lead'), ('PM', 'Project Manager'), ('OT', 'Other')])),
                ('is_first_login', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
