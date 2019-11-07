from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{0} {1}".format(self.id, self.name)
    
class Score(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, null=False, blank=False, on_delete= models.CASCADE)
    student = models.ForeignKey(Student,  null=False, blank=False, on_delete = models.CASCADE)
    value = models.CharField(max_length=50)
    
    def __str__(self):
        return "{0} {1}".format(self.id, self.name)
