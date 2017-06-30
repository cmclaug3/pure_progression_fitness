# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Fitness.models import Exercise, Workout, WorkoutSet, CardioSet

admin.site.register(Exercise)
admin.site.register(CardioSet)

class WorkoutSetInLine(admin.StackedInline):
	model = WorkoutSet


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
	inlines = (WorkoutSetInLine, )
