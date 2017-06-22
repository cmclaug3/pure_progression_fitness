from django.conf.urls import url, include
from django.contrib import admin
from Fitness.views import home, single_workout

urlpatterns = [
	url(r'^workout/(?P<workout_id>[0-9]+)$', single_workout, name='single_workout'),
	url(r'^$', home, name='home'),
]