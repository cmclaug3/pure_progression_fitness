# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0004_workoutset_sets'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='theme',
            field=models.CharField(blank=True, choices=[('arms', 'Arms'), ('legs', 'Legs'), ('chest', 'Chest'), ('shoulders', 'Shoulders'), ('back', 'Back'), ('core', 'Core'), ('cardio', 'Cardio')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='body_part',
            field=models.CharField(choices=[('arms', 'Arms'), ('legs', 'Legs'), ('chest', 'Chest'), ('shoulders', 'Shoulders'), ('back', 'Back'), ('core', 'Core'), ('cardio', 'Cardio')], max_length=50),
        ),
    ]