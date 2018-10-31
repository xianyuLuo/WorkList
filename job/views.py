from job.serializers import LevelSerializer, JobSerializer
from job.models import level, job
from rest_framework import generics

class LevelList(generics.ListCreateAPIView):
    queryset = level.objects.all()
    serializer_class = LevelSerializer

class JobList(generics.ListCreateAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer
