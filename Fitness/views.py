# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from Fitness.models import Exercise, Workout, WorkoutSet
from Fitness.forms import WorkoutSetForm, WorkoutForm, ExerciseForm, CardioSetForm

# stuff for the restAPI
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Fitness.serializers import WorkoutSetSerializer

from django.contrib.auth.decorators import login_required


def home(request):
	if not request.user.is_authenticated:
		return redirect(reverse('account_login'))
	context = {
		'workouts': Workout.objects.filter(user=request.user)
	}
	return render(request, 'home.html', context)


def single_workout(request, workout_id):
	if not request.user.is_authenticated:
		return redirect(reverse('account_login'))

	workout = Workout.objects.get(user=request.user, pk=workout_id)
	context = {
		'workout': workout,
	}
	return render(request, 'single_workout.html', context)



@login_required
def workout_set_submit(request):
	form_class = WorkoutSetForm
	form = form_class(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			#if request.POST.get('sibmut2', False):
				#return redirect('workout_form')
			return redirect('home')
		else:
			form = WorkoutSetForm()
	context = {
		'form': form,
	}

	return render(request, 'workout_set_form.html', context)



@login_required
def workout_form(request):
	form_class = WorkoutForm
	form2 = form_class(request.POST or None)
	incorrect = ''
	if request.method == 'POST':
		if form2.is_valid():
			form2.save()
		else:
			form2 = WorkoutForm()
			incorrect = 'Something went wrong, try again..'
	context = {
		'form2': form2,
		'incorrect': incorrect,
	}

	return render(request, 'workout_form.html', context)


# not being used yet, possibly used to redirect to a draft of workout
# to see if the user is ok with it before submitting
def workout_review(request):
	context = {

	}
	return render(request, 'workout_review.html', context)



#Lists all workout sets or creates a new one/restAPI JSON
@login_required
class WorkoutSetList(APIView):

	def get(self, request):
		workoutset = WorkoutSet.objects.all()
		serializer = WorkoutSetSerializer(workoutset, many=True)
		return Response(serializer.data)

	def post(self):
		pass


def cardio_set_form(request):
	form = CardioSetForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			form.save()

			return redirect('home')
		else:
			form = WorkoutSetForm()
	context = {
		'form': form,
	}

	return render(request, 'cardio_set_form.html', context)





