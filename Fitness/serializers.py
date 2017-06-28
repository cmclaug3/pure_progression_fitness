from rest_framework import serializers
from Fitness.models import WorkoutSet

class WorkoutSetSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkoutSet
		fields = ('reps', 'load', 'intensity')