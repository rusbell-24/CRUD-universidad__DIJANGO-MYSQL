from django.db import models

# Create your models here.

class Career(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    careerStatus = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class Course(models.Model):
    id = models. AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    credit = models.IntegerField()
    courseStatus = models.BooleanField(default=True)
    
    career = models.ManyToManyField('Career')
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    dni= models.CharField(max_length=20)
    birthDate = models.DateField()
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models. CharField(max_length=100, null=True, blank=True)
    dniFile = models.FileField()
    teacherStatus = models.BooleanField(default=True)
    
    course = models.ForeignKey(Course, default=1, on_delete = models.CASCADE)
    
    def __str__(self):
        return "nombre: " + self.name + "CC: " + self.dni
    

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    dni= models.CharField(max_length=20)
    birthDate = models.DateField()
    name = models.CharField(max_length=100, null=True, blank=True)
    gender = models. CharField(max_length=100, null=True, blank=True)
    dniFile = models.FileField()
    studentStatus = models.BooleanField(default=True)
    
    course = models.ManyToManyField('Course')
    
    def __str__(self):
        return "nombre: " + self.name + "CC: " + self.dni
    
    

