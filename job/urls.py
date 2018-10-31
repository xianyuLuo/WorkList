from django.urls import path
from job import views

urlpatterns = [
    path('levellist/', views.LevelList.as_view(), name = 'levellist'),
    path('joblist/', views.JobList.as_view(), name = 'joblist'),
]