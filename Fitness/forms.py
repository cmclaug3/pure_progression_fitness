from django import forms
from Fitness.models import WorkoutSet, Workout, Exercise, CardioSet

class WorkoutSetForm(forms.ModelForm):
	class Meta:
		model = WorkoutSet
		fields = [
			'workout', 'exercise', 'sets', 'reps', 'load',
			'intensity', 'notes',
		]

class WorkoutForm(forms.ModelForm):
	class Meta:
		model = Workout
		fields = [
			'user', 'theme', 'date', 'notes',
		]

class ExerciseForm(forms.ModelForm):
	class Meta:
		model = Exercise
		fields = '__all__'

class CardioSetForm(forms.ModelForm):
	class Meta:
		model = CardioSet
		fields = '__all__'