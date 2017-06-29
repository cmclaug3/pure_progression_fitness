from django import forms
from Fitness.models import WorkoutSet, Workout, Exercise

class WorkoutSetForm(forms.ModelForm):
	class Meta:
		model = WorkoutSet
		fields = [
			'workout', 'exercise', 'reps',
			'rep_style', 'notes', 'intensity', 'load'
		]

class WorkoutForm(forms.ModelForm):
	class Meta:
		model = Workout
		fields = [
			'date', 'user', 'notes',
		]

class ExerciseForm(forms.ModelForm):
	class Meta:
		model = Exercise
		fields = '__all__'