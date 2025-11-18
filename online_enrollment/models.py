from django.db import models
from datetime import date
# Create your models here.
class Student (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    date_birth=models.DateField(blank=True,null=True)
    address=models.CharField(max_length=100)
    student_id=models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'

class Course (models.Model):
    course_id=models.CharField(max_length=10)
    head_of_department=models.CharField(max_length=100)
    no_of_professors=models.IntegerField()
    no_of_students=models.IntegerField()
    units_per_sem=models.IntegerField()
    def __str__(self):
        return f'{self.course_id}'

    
class Instructor (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.IntegerField()
    department=models.CharField(max_length=100)
    instructor_id=models.IntegerField()
    def __str__(self):
        return f'{self.name}'

    
class Subject (models.Model):
    name=models.CharField(max_length=100)
    no_units=models.IntegerField()
    semesters=models.IntegerField()
    schedule=models.DateField(blank=True,null=True)
    subject_id=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
    
class Schedule(models.Model):
    room=models.CharField(max_length=10)
    instructor_id=models.IntegerField()
    students_per_dept=models.IntegerField()
    subject_id=models.CharField(max_length=100)
    day_time=models.DateField(blank=True,null=True)
    def __str__(self):
        return f'{self.room}'
