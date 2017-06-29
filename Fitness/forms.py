from django import forms
from Fitness.models import WorkoutSet, Workout, Exercise

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