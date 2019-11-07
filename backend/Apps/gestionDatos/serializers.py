from rest_framework import serializers
from .models import Student,Score,Professor

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields= ('id','name')
        
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Professor
        fields= ('id','name')
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Score
        fields= ('id','name','professor','student','value')