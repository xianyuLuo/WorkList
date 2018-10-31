from rest_framework import serializers
from job.models import job, level

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = level
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    job_level = serializers.CharField(source = 'job_level.level_name')
    class Meta:
        model = job
        fields = ('job_level', 'job_date', 'job_content', 'job_isover', 'job_comment')