# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fitness', '0010_auto_20170629_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardioSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(choices=[('run', 'Run'), ('spring', 'Sprint'), ('swim', 'Swim'), ('ellyptical', 'Ellyptical'), ('heavy-bag', 'Heavy Bag'), ('row-machine', 'Row Machine')], max_length=25)),
                ('time_length', models.TimeField()),
                ('speed', models.FloatField()),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fitness.Workout')),
            ],
        ),
        migrations.AlterField(
            model_name='workoutset',
            name='load',
            field=models.IntegerField(help_text='Weight in pounds'),
        ),
        migrations.AlterField(
            model_name='workoutset',
            name='sets',
            field=models.IntegerField(default=1, help_text='Number of sets'),
        ),
    ]
