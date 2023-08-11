from django.contrib import admin

# Register your models here.

from .models import *

class CareerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'careerStatus')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'credit', 'courseStatus')
    
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','dni', 'birthDate', 'name', 'gender', 'dniFile', 'teacherStatus')
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','dni', 'birthDate', 'name', 'gender', 'dniFile', 'studentStatus')
    

admin.site.register(Career, CareerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
