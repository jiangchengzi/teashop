# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-01 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=200)),
                ('User_password', models.CharField(max_length=200)),
            ],
        ),
    ]
