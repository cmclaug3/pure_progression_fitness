from django.conf.urls import url, include
from django.contrib import admin
from Fitness.views import home, single_workout, workout_set_submit

urlpatterns = [
	url(r'^workout/(?P<workout_id>[0-9]+)$', single_workout, name='single_workout'),
	url(r'^$', home, name='home'),
	url(r'^new_set', workout_set_submit, name='workout_set_submit'),
]