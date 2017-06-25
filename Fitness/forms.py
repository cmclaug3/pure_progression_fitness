from django import forms
from Fitness.models import WorkoutSet

class WorkoutSetForm(forms.ModelForm):
	class Meta:
		model = WorkoutSet
		fields = [
			'workout', 'exercise', 'reps',
			'rep_style', 'notes', 'intensity', 'load'
		]