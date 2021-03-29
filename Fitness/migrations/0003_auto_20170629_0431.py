# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0002_auto_20170622_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutset',
            name='rep_style',
            field=models.CharField(choices=[('str', 'Strength'), ('hypertrophy', 'Hypertrophy'), ('power', 'Power'), ('endurance', 'Endurance')], max_length=15),
        ),
    ]