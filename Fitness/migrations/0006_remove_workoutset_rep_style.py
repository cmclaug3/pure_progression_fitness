# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0005_auto_20170629_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutset',
            name='rep_style',
        ),
    ]
