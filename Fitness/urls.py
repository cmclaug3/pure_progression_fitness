from django.conf.urls import url, include
from django.contrib import admin
from Fitness.views import home, single_workout, workout_set_submit, workout_form

urlpatterns = [

	url(r'^workout/(?P<workout_id>[0-9]+)$', single_workout, name='single_workout'),
	url(r'^new_set', workout_set_submit, name='workout_set_submit'),
	url(r'^new_workout', workout_form, name='workout_form'),
	url(r'^$', home, name='home'),
	
	]