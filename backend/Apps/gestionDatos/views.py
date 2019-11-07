from django.shortcuts import render
from rest_framework import viewsets
from .models import Professor,Score,Student
from .serializers import StudentSerializer, ProfessorSerializer, ScoreSerializer

# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    
class ProfessorView(viewsets.ModelViewSet):
    queryset= Professor.objects.all()
    serializer_class = ProfessorSerializer
    
class ScoreView(viewsets.ModelViewSet):
    queryset= Score.objects.all()
    serializer_class = ScoreSerializer