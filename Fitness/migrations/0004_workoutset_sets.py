# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0003_auto_20170629_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutset',
            name='sets',
            field=models.IntegerField(default=1, help_text='number of sets'),
        ),
    ]
