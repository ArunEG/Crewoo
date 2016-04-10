# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, parent_link=True, serialize=False, primary_key=True, auto_created=True)),
                ('gender', models.CharField(verbose_name='Gender', max_length=1, choices=[('F', 'Female'), ('M', 'Male')])),
                ('image', models.ImageField(verbose_name='Image', upload_to='Staffs/', null=True, blank=True)),
                ('mobile', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.TextField(verbose_name='Address', null=True, blank=True)),
                ('dob', models.DateField(verbose_name='DOB', null=True, blank=True)),
                ('user_type', models.CharField(max_length=2, default='OT', choices=[('TL', 'Team Lead'), ('PM', 'Project Manager'), ('OT', 'Other')])),
                ('is_first_login', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staffs',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
