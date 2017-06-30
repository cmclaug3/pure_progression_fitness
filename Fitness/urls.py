from django.conf.urls import url, include
from django.contrib import admin
from Fitness.views import home, single_workout, workout_set_submit, workout_form, cardio_set_form
from rest_framework.urlpatterns import format_suffix_patterns
from Fitness import views

urlpatterns = [

	url(r'^workout/(?P<workout_id>[0-9]+)$', single_workout, name='single_workout'),
	url(r'^new_set', workout_set_submit, name='workout_set_submit'),
	url(r'^new_workout', workout_form, name='workout_form'),
	url(r'^cardio_set', cardio_set_form, name='cardio_set_form'),
	#url(r'^workoutset/', views.WorkoutSetList.as_view()),
	url(r'^$', home, name='home'),
	
	]

urlpatterns = format_suffix_patterns(urlpatterns)